__author__ = 'singo'
__datetime__ = '2019/4/28 9:57 PM '


import time
from django.core.cache import cache
from functools import wraps
from django.conf import settings
import json
from django.db import connections
from ast import literal_eval

from common.apscheduler import my_scheduler_run_now
from common.apis import jenkins_api, dingtalk_chatbot
from .models import History, TYPE
from datetime import datetime, timedelta
from .common import *
from common.apis import saltapi, gitlab_api
from common.utils import update_cache_value, update_obj, logger



class DeployJob(object):
    def __init__(self, cache_name, order_obj, assign_to):
        self.cache_name = cache_name
        self.order_obj = order_obj
        self.deploy_cache = cache.get(cache_name, {})
        self.his_obj = None
        self.f = None
        self.assign_to = assign_to
        # 设置第几次执行上线单
        self.order_obj.deploy_times += 1
        self.minion = settings.DEPLOY.get('M_MINION')

        for conn in connections.all():
            conn.close_if_unusable_or_obsolete()

    def init_job(self):
        # 上线工单需要获取最新分支信息
        try:
            if self.order_obj.type != ROLLBACK:
                branch_info = gitlab_api.get_branch_info(self.order_obj.project.gitlab_project, self.order_obj.branche)
                commit_id = branch_info.commit.get('id')
                commit = branch_info.commit.get('message')
                # 设置版本号
                self.order_obj.version = self.order_obj.project.version
            else:
                raise Exception
        except Exception as e:
            logger.exception(e)
            commit_id = self.order_obj.commit_id
            commit = self.order_obj.commit

        self.f = open(self.deploy_cache.get('log'), 'a')
        # 记录日志
        self.his_obj = History.objects.create(
            **{
                'order_id': self.order_obj.id,
                'deploy_times': self.order_obj.deploy_times,
                'title': self.order_obj.title,
                'project_name': self.order_obj.project.name,
                'env': self.order_obj.env.name,
                'type': self.order_obj.type,
                'servers_ip': self.order_obj.servers_ip,
                'servers_saltID': self.order_obj.servers_saltID,
                'branche': self.order_obj.branche,
                'commit_id': commit_id,
                'commit': commit,
                'jk_number': -1,
                'applicant': self.order_obj.applicant.name,
                'reviewer': self.order_obj.reviewer.name,
                'assign_to': self.assign_to,
                'log_file': self.deploy_cache.get('log'),
                'result': H_UNKNOWN
            }
        )

    def __jenkins_log(self, job_name, build_number, line_number):
        log = jenkins_api.get_build_console_output(job_name, build_number)
        log = log.splitlines()
        self.f.write('\n'.join(log[line_number:]))

        if (len(log) > line_number):
            self.f.write('\n')

        self.f.flush()
        return len(log)

    def __deal_with_salt_ret(self, rets):
        """
        判断sls是否执行成功
        :param rets:
        :return: {'saltid':bool,...}
        """
        brief = {}
        rets = rets.get('return', [])

        for ret in rets:
            try:
                for salt_id, contents in ret.items():
                    try:
                        for content in contents.values():
                            if content.get('result') and content.get('__id__') == 'finally':
                                brief[salt_id] = True
                                break
                    except:
                        brief[salt_id] = False
            except:
                continue
        return brief

    # 生成docker镜像
    def make_docker_image(self):
        if self.order_obj.project.deploy_type != DOCKER:
            return None
        
        logger.debug('开始生成docker镜像')
        self.f.write('> 开始生成docker镜像\n')
        self.f.flush()

        minion = settings.DEPLOY.get('M_MINION')

        rets = saltapi.state_sls(minion, **{
            'pillar':
                {'project': self.order_obj.project.name,
                 'env': self.order_obj.env.code,
                 'tag': self.order_obj.version
                 },
            'mods': 'make_docker_image',
            'saltenv': 'deploy'
        })

        self.f.write(json.dumps(rets, indent=4))
        logger.debug('执行生成docker镜像完成')
        self.f.write('\n> 执行生成docker镜像完成\n')
        self.f.flush()

        rets = rets.get('return', [])[0].get(minion)

        for k, v in rets.items():
            if not v.get('result'):
                raise Exception('生成docker镜像失败')


    @staticmethod
    def set_step_cache(cache_name, deploy_cache):
        deploy_cache['current_step'] += 1
        cache.set(cache_name, deploy_cache, timeout=CACHE_TIMEOUT)
        logger.debug(str(deploy_cache))

    # 构建
    def build(self):
        # 回滚需要先从历史记录获取jenkins的build_number
        if self.order_obj.type == ROLLBACK:
            try:
                history = History.objects.get(pk=self.order_obj.content)
                build_number = history.jk_number
            except:
                raise Exception('获取回滚版本信息失败')
        else:
            logger.debug('开始构建项目')
            self.f.write('> 开始构建项目\n')
            self.f.flush()

            line_number = 0
            job_name = self.order_obj.project.jenkins_job
            build_number = jenkins_api.get_next_build_number(job_name)
            # 获取jenkins参数
            parameters = literal_eval(self.order_obj.project.jenkins_params)
            parameters['BRANCH'] = self.order_obj.branche
            parameters['ENV'] = self.order_obj.sub_env_code
            # queue_id = jenkins_api.build_job(job_name, parameters={'BRANCH': self.order_obj.branche, 'ENV':  self.order_obj.env.code})
            try:
                queue_id = jenkins_api.build_job(job_name, parameters=parameters)
            except Exception as e:
                logger.exception(e)
                self.f.write('> 启动jenkins任务失败\n')
                self.f.write(str(e))
                self.f.flush()
                raise Exception('启动jenkins任务失败')

            update_cache_value(self.cache_name, self.deploy_cache, **{'build_number': build_number})
            self.set_step_cache(self.cache_name, self.deploy_cache)

            # 最多等待 jenkins 20分
            for i in range(240):
                time.sleep(5)
                build_info = jenkins_api.get_build_info(job_name, build_number)

                if build_info and queue_id != build_info.get('queueId'):
                    raise Exception('获取jenkins build number 失败')
                # 构建中
                elif build_info and build_info.get('building') == True:
                    logger.debug('构建中')
                    # 获取jenkins日志
                    line_number = self.__jenkins_log(job_name, build_number, line_number)
                    continue
                # 构建成功
                elif build_info and build_info.get('building') == False and build_info.get('result') == 'SUCCESS':
                    logger.debug('构建完成')
                    self.__jenkins_log(job_name, build_number, line_number)
                    update_obj(self.his_obj, **{'jk_result': build_info.get('result')})
                    break
                # 构建失败
                elif build_info and build_info.get('building') == False and build_info.get('result') != 'SUCCESS':
                    logger.debug('构建失败')
                    self.__jenkins_log(job_name, build_number, line_number)
                    update_obj(self.his_obj, **{'jk_result': build_info.get('result')})
                    raise Exception('构建失败')
                # 构建未开始
                else:
                    logger.debug('等待jenkins创建任务')
            self.f.write('> 构建完成\n')
            self.f.flush()

        update_obj(self.his_obj, **{'jk_number': build_number})

    # 下载代码包
    def download_package(self):
        logger.debug('开始下载代码')
        self.f.write('> 开始下载代码\n')
        self.f.flush()

        build_number = self.deploy_cache['build_number']

        self.set_step_cache(self.cache_name, self.deploy_cache)
        jenkins_api.download_package(self.order_obj.project.package_url,
                                     self.order_obj.project.jenkins_job,
                                     build_number)

        logger.debug('代码下载完成')
        self.f.write('> 代码下载完成\n')
        self.f.flush()

    # 执行sls文件
    def deploy_state_sls(self):
        logger.debug('开始执行salt SLS')
        self.f.write('> 开始执行salt SLS\n')
        self.f.flush()

        salt_id_list = [s.saltID for s in self.order_obj.get_deploy_servers]

        rets = saltapi.state_sls(salt_id_list, **{
            'pillar':
                {'project': self.order_obj.project.name,
                 'order_id': str(self.order_obj.id),
                 'env': self.order_obj.env.code,
                 'devops_env': settings.ENV,
                 'private_vars': self.order_obj.get_private_vars
                 },
            'mods': self.order_obj.project.name,
            'saltenv': 'deploy'
        })

        self.f.write(json.dumps(rets, indent=4))
        logger.debug('salt SLS 执行完成')
        self.f.write('\n> salt SLS 执行完成\n')
        self.f.flush()

        brief = self.__deal_with_salt_ret(rets)

        for salt_id in salt_id_list:
            if brief.get(salt_id, 'default') == 'default':
                brief[salt_id] = False

        failed_salt = [k for k, v in brief.items() if v == False]

        if failed_salt:
            raise Exception('{}执行salt sls失败'.format(','.join(failed_salt)))

    # 部署完成后的状态处理
    def end_job(self, order_data=None, his_data=None, cache_data=None, write_msg=''):
        deploy_cache = cache.get(self.cache_name, {})

        # 发布成功需要设置下一次版本号
        if self.order_obj.status == D_SUCCESSFUL:
            update_obj(self.order_obj.project, **{'version': self.order_obj+0.01})

        update_obj(self.order_obj, **order_data)
        update_cache_value(self.cache_name, deploy_cache, **cache_data)
        self.his_obj and update_obj(self.his_obj, **his_data)

        if self.f:
            self.f.write('> {}\nEOF'.format(write_msg))
            self.f.flush()
            self.f.close()


def timings(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            order_obj = args[1]
            dingtalk_chatbot.text_msg('{}开始{} {}'.format(order_obj.env.name,
                                                        TYPE[order_obj.type][1],
                                                        order_obj.project.name)
                                      )
            realtime_log_url = '{}/deploy/log/{}'.format(settings.FRONT_END_URL, order_obj.id)
            dingtalk_chatbot.send_link('实时日志', '点击查看日志', realtime_log_url)
        except Exception as e:
            logger.exception(e)

        start = time.time()
        ret = f(*args, **kwargs)
        s_ret = '成功' if ret else '失败'
        end = time.time()
        elapsed_time = round((end - start), 0)

        dingtalk_chatbot.text_msg('{}{}{}{},耗时 {}'.format(order_obj.env.name,
                                                                order_obj.project.name,
                                                                TYPE[order_obj.type][1],
                                                                s_ret,
                                                                timedelta(seconds=elapsed_time))
                                  )
    return wrapper

@my_scheduler_run_now('date')
@timings
def start_job(cache_name, order_obj, assign_to, *args, **kwargs):
    try:
        deploy_job = DeployJob(cache_name, order_obj, assign_to)

        deploy_job.init_job()

        #################jenkins构建################
        deploy_job.build()

        ###################生成镜像##################
        deploy_job.make_docker_image()

        ###################下载代码##################
        deploy_job.download_package()

        ##################执行SLS文件################
        deploy_job.deploy_state_sls()

        ##################完成发布################
        deploy_job.end_job(order_data={'status': D_SUCCESSFUL, 'result_msg': '上线完成', 'complete_time': datetime.now()},
                his_data={'result': H_SUCCESSFUL, 'end': datetime.now()},
                cache_data={'is_lock': False, 'status': S_SUCCESSFUL},
                write_msg='部署成功'
                )

        return True

    except Exception as e:
        logger.exception(e)
        deploy_job.end_job(order_data={'status': D_FAILED, 'result_msg': str(e), 'complete_time': datetime.now()},
                his_data={'result': H_FAILED, 'error_msg': str(e), 'end': datetime.now()},
                cache_data={'is_lock': False, 'status': S_FAILED},
                write_msg='部署失败'
                )
        return False


# def timings(*args, **kwargs):
#     def wrapper(f):
#         def inner(*a, **k):
#             start = time()
#             f(*a, **k)
#             end = time()
#             elapsed_time = round((end - start), 2)
#         return inner
#     return wrapper


@my_scheduler_run_now('date')
def test_start_job(cache_name, order_obj, assign_to, *args, **kwargs):
    # scheduler.remove_job(job_id)
    # kwargs.get('job_id')
    # time.sleep(10)
    print('end')