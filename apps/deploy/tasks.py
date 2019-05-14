__author__ = 'singo'
__datetime__ = '2019/4/28 9:57 PM '


import time
from django.core.cache import cache
from functools import wraps
from django.conf import settings

from common.apscheduler import my_scheduler_run_now
from common.apis import jenkins_api, dingtalk_chatbot
from common.utils import logger
from .models import History
from datetime import datetime, timedelta
from .common import *
from common.apis import saltapi



def save_order_obj(order_obj, **kwargs):
    order_obj.__dict__.update(**kwargs)
    order_obj.save()

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
    cache.set(cache_name, deploy_cache, timeout=24*3600)

def create_or_update_history(order_obj=None, deploy_cache=None, obj=None, **kwargs):
    try:
        if obj:
            obj.__dict__.update(**kwargs)
            obj.save()
        else:
            obj = History.objects.create(
                    **{
                        'order_id': order_obj.id,
                        'deploy_times': order_obj.deploy_times,
                        'title': order_obj.title,
                        'project_name': order_obj.project.name,
                        'env': order_obj.env,
                        'type': 0,
                        'servers_ip': order_obj.project.servers_ip,
                        'servers_saltID':order_obj.project.servers_saltID,
                        'branche': order_obj.branche,
                        'commit_id': order_obj.commit_id,
                        'commit': order_obj.commit,
                        'jk_number': deploy_cache.get('build_number'),
                        'applicant': order_obj.applicant.name,
                        'reviewer': order_obj.reviewer.name,
                        'assign_to': order_obj.assign_to.name,
                        'log_file': deploy_cache.get('log'),
                    }
            )
            return obj
    except Exception as e:
        logger.exception(e)
        logger.error(e)


def deal_with_salt_ret(rets):
    """
    判断sls是否执行成功
    :param rets:
    :return: {'saltid':bool,...}
    """
    brief = {}

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
def build(f, cache_name, deploy_cache, history):
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
            create_or_update_history(obj=history, **{'jk_result': build_info.get('result')})
            break
        # 构建失败
        elif build_info and build_info.get('building') == False and build_info.get('result') != 'SUCCESS':
            logger.debug('构建失败')
            jenkins_log(f, job_name, build_number, line_number)
            create_or_update_history(obj=history, **{'jk_result': build_info.get('result')})
            raise Exception('构建失败')
        # 构建未开始
        else:
            logger.debug('等待jenkins创建任务')

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

# 执行sls文件
def deploy_state_sls(f, order_obj):
    logger.debug('开始执行salt SLS')
    f.write('> 开始执行salt SLS\n')
    f.flush()

    salt_id = [s.saltID for s in order_obj.project.servers.all()]

    rets = saltapi.state_sls(salt_id, **{
        'mods': order_obj.project.name,
        'saltenv': 'deploy'
    })
    f.write(str(rets))
    f.flush()

    rets = rets.get('return', [])
    brief = deal_with_salt_ret(rets)

    for s in salt_id:
        if brief.get(s, 'default') == 'default':
            brief[s] = False

    if len([k for k, v in brief.items() if v == False]) > 0 :
        raise Exception('存在执行SLS失败的主机')

def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            order_obj = args[1]
            dingtalk_chatbot.text_msg('开始上线项目 {}'.format(order_obj.project.name))
            realtime_log_url = '{}/log.html?id={}'.format(settings.FRONT_END_URL, order_obj.id)
            dingtalk_chatbot.send_link('上线实时日志', '点击查看日志', realtime_log_url)
        except Exception as e:
            logger.exception(e)

        start = time.time()
        f(*args, **kwargs)
        end = time.time()

        elapsed_time = round((end - start), 0)

        dingtalk_chatbot.text_msg('{}已完成上线,耗时 {}'.format(order_obj.project.name, timedelta(seconds=elapsed_time)))
    return wrapper

@my_scheduler_run_now('date')
@timing
def start_job(cache_name, order_obj, assign_to):
    try:
        # 设置第几次执行上线单
        order_obj.deploy_times += 1
        deploy_cache = cache.get(cache_name, {})
        # 记录日志
        history = create_or_update_history(order_obj, deploy_cache)
        f = open(deploy_cache['log'], 'a')

        #################jenkins构建################
        build(f, cache_name, deploy_cache, history)

        ###################下载代码##################
        download_package(f, cache_name, deploy_cache, order_obj)

        ##################执行SLS文件################
        deploy_state_sls(f, order_obj)

        ##################完成发布################
        print(deploy_cache)
        print(order_obj.title)

        create_or_update_history(obj=history, **{'result': SUCCESSFUL, 'end': datetime.now()})
        save_order_obj(order_obj, **{'status': ONLINED})

    except Exception as e:
        logger.exception(e)
        save_order_obj(order_obj, **{'result': str(e), 'status': FAIL})
        kwargs = {
            'result': FAILED,
            'error_msg': str(e),
            'end': datetime.now()
        }
        create_or_update_history(obj=history, **kwargs)
        return False


# def timing(*args, **kwargs):
#     def wrapper(f):
#         def inner(*a, **k):
#             start = time()
#             f(*a, **k)
#             end = time()
#             elapsed_time = round((end - start), 2)
#         return inner
#     return wrapper
