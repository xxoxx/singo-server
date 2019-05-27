__author__ = 'singo'
__datetime__ = '2019/4/28 9:57 PM '


import time
from django.core.cache import cache
from functools import wraps
from django.conf import settings

from common.apscheduler import my_scheduler_run_now
from common.apis import jenkins_api, dingtalk_chatbot
from .models import History, ENV, TYPE, HISTORY_STATUS
from datetime import datetime, timedelta
from .common import *
from common.apis import saltapi
from common.utils import update_cache_value, update_obj, logger




def jenkins_log(f, job_name, build_number, line_number):
    log = jenkins_api.get_build_console_output(job_name, build_number)
    log = log.splitlines()
    f.write('\n'.join(log[line_number:]))

    if (len(log) > line_number):
        f.write('\n')

    f.flush()
    return len(log)

def set_step_cache(cache_name, deploy_cache):
    deploy_cache['current_step'] += 1
    cache.set(cache_name, deploy_cache, timeout=CACHE_TIMEOUT)
    logger.debug(str(deploy_cache))

def deal_with_salt_ret(rets):
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


# 构建
def build(f, cache_name, deploy_cache, his_obj):
    logger.debug('开始构建项目')
    f.write('> 开始构建项目\n')
    f.flush()

    line_number = 0
    set_step_cache(cache_name, deploy_cache)
    job_name = deploy_cache['job_name']
    build_number = deploy_cache['build_number']
    queue_id = deploy_cache.get('queue_id')

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
            line_number = jenkins_log(f, job_name, build_number, line_number)
            continue
        # 构建成功
        elif build_info and build_info.get('building') == False and build_info.get('result') == 'SUCCESS':
            logger.debug('构建完成')
            jenkins_log(f, job_name, build_number, line_number)
            update_obj(his_obj, **{'jk_result': build_info.get('result')})
            break
        # 构建失败
        elif build_info and build_info.get('building') == False and build_info.get('result') != 'SUCCESS':
            logger.debug('构建失败')
            jenkins_log(f, job_name, build_number, line_number)
            update_obj(his_obj, **{'jk_result': build_info.get('result')})
            raise Exception('构建失败')
        # 构建未开始
        else:
            logger.debug('等待jenkins创建任务')

    f.write('> 构建完成\n')
    f.flush()

# 下载代码包
def download_package(f, cache_name, deploy_cache, order_obj):
    logger.debug('开始下载代码')
    f.write('> 开始下载代码\n')
    f.flush()

    build_number = deploy_cache['build_number']

    set_step_cache(cache_name, deploy_cache)
    jenkins_api.download_package(order_obj.project.package_url,
                                 order_obj.project.jenkins_job,
                                 build_number)

    logger.debug('代码下载完成')
    f.write('> 代码下载完成\n')
    f.flush()

# 执行sls文件
def deploy_state_sls(f, order_obj):
    logger.debug('开始执行salt SLS')
    f.write('> 开始执行salt SLS\n')
    f.flush()

    salt_id_list = [s.saltID for s in order_obj.project.servers.all()]

    rets = saltapi.state_sls(salt_id_list, **{
        'pillar':
            {   'project': order_obj.project.name,
                'order_id': str(order_obj.id),
                'env': S_ENV[order_obj.env][1],
                'devops_env': settings.ENV
            },
        'mods': order_obj.project.name,
        'saltenv': 'deploy',
    })
    f.write(str(rets)+'\n')
    logger.debug('salt SLS 执行完成')
    f.write('> salt SLS 执行完成\n')
    f.flush()

    brief = deal_with_salt_ret(rets)

    for salt_id in salt_id_list:
        if brief.get(salt_id, 'default') == 'default':
            brief[salt_id] = False

    failed_salt = [k for k, v in brief.items() if v == False]

    if failed_salt:
        raise Exception('{}执行salt sls失败'.format(','.join(failed_salt)))

# 部署完成后的状态处理
def end_job(f, cache_name, order_obj, his_obj, order_data=None, his_data=None, cache_data=None, write_msg=''):
    deploy_cache = cache.get(cache_name, {})

    update_obj(order_obj, **order_data)
    update_cache_value(cache_name, deploy_cache, **cache_data)
    his_obj and update_obj(his_obj, **his_data)

    if f:
        f.write('> {}\n'.format(write_msg))
        f.flush()
        f.close()

def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            order_obj = args[1]
            dingtalk_chatbot.text_msg('{}开始{} {}'.format(ENV[order_obj.env][1],
                                                        TYPE[order_obj.type][1],
                                                        order_obj.project.name)
                                      )
            # realtime_log_url = '{}/log.html?id={}'.format(settings.FRONT_END_URL, order_obj.id)
            realtime_log_url = '{}/deploy/log/{}'.format(settings.FRONT_END_URL, order_obj.id)
            dingtalk_chatbot.send_link('实时日志', '点击查看日志', realtime_log_url)
        except Exception as e:
            logger.exception(e)

        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        elapsed_time = round((end - start), 0)

        his_obj = History.objects.get(order_id=order_obj.id, deploy_times=order_obj.deploy_times)

        dingtalk_chatbot.text_msg('{}{}{}{},耗时 {}'.format(ENV[order_obj.env][1],
                                                                order_obj.project.name,
                                                                TYPE[order_obj.type][1],
                                                                HISTORY_STATUS[his_obj.result][1],
                                                                timedelta(seconds=elapsed_time))
                                  )
    return wrapper

@my_scheduler_run_now('date')
@timing
def start_job(cache_name, order_obj, assign_to, *args, **kwargs):
    try:
        # 设置第几次执行上线单
        order_obj.deploy_times += 1
        deploy_cache = cache.get(cache_name, {})
        his_obj = None
        f = None

        try:
            # 记录日志
            his_obj = History.objects.create(
                **{
                    'order_id': order_obj.id,
                    'deploy_times': order_obj.deploy_times,
                    'title': order_obj.title,
                    'project_name': order_obj.project.name,
                    'env': order_obj.env,
                    'type': order_obj.type,
                    'servers_ip': order_obj.project.servers_ip,
                    'servers_saltID': order_obj.project.servers_saltID,
                    'branche': order_obj.branche,
                    'commit_id': order_obj.commit_id,
                    'commit': order_obj.commit,
                    'jk_number': deploy_cache.get('build_number'),
                    'applicant': order_obj.applicant.name,
                    'reviewer': order_obj.reviewer.name,
                    'assign_to': assign_to,
                    'log_file': deploy_cache.get('log'),
                }
            )

            f = open(deploy_cache.get('log'), 'a')

        except Exception as e:
            jenkins_api.cancel_build(deploy_cache.get('job_name'), deploy_cache.get('queue_id'), deploy_cache.get('build_number'))
            raise e


        if order_obj.type != ROLLBACK:
            #################jenkins构建################
            build(f, cache_name, deploy_cache, his_obj)

        ###################下载代码##################
        download_package(f, cache_name, deploy_cache, order_obj)

        ##################执行SLS文件################
        deploy_state_sls(f, order_obj)

        ##################完成发布################
        end_job(f, cache_name, order_obj, his_obj,
                order_data={'status': D_SUCCESSFUL, 'result_msg': '上线完成', 'complete_time': datetime.now()},
                his_data={'result': H_SUCCESSFUL, 'end': datetime.now()},
                cache_data={'is_lock': False, 'status': S_SUCCESSFUL},
                write_msg='部署成功'
                )

    except Exception as e:
        logger.exception(e)
        end_job(f, cache_name, order_obj, his_obj,
                order_data={'status': D_FAILED, 'result_msg': str(e), 'complete_time': datetime.now()},
                his_data={'result': H_FAILED, 'error_msg': str(e), 'end': datetime.now()},
                cache_data={'is_lock': False, 'status': S_FAILED},
                write_msg='部署失败'
                )


# def timing(*args, **kwargs):
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
    # from django.core.cache import cache
    # job_id = cache.get('deploy.tasks.test_start_job')
    # print(job_id)
    # print('test_start_job')
    # scheduler.remove_job(job_id)
    kwargs.get('job_id')
    time.sleep(10)
    print('end')