__author__ = 'singo'
__datetime__ = '2019/4/28 10:42 AM'


from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django.conf import settings
import os, time, linecache
from rest_framework.exceptions import APIException
from datetime import datetime

from common.utils import logger, update_cache_value, update_obj
from common.permissions import DevopsPermission, DeployPermission, IsDevopsPermission
from ..models import DeploymentOrder
from common.apis import jenkins_api, saltapi
from ..tasks import start_job, set_step_cache
from ..common import *
from ..models import History



class DeployError(APIException):
    status_code = 403
    default_detail = 'deploy error'
    default_code = 'invalid'


class BaseDeployAPIView(APIView):

    def get_object(self):
        obj = get_object_or_404(DeploymentOrder, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class DeployJob(BaseDeployAPIView):
    """
    项目上线

    post:
        启动上线

    get:
        获取上线状态
    """
    permission_classes = (permissions.IsAuthenticated, DeployPermission)


    def check_deploy(self, order_obj, deploy_cache):
        # 避免被重复执行部署
        if deploy_cache.get('is_lock'):
            raise DeployError('该任务已经启动')
        elif order_obj.status != 1:
            raise DeployError('该工单状态不能上线')
        return True


    def __init_jenkins(self, order_obj, jenkins_job_name):
        if order_obj.type != ROLLBACK:
            build_number = jenkins_api.get_next_build_number(jenkins_job_name)
            queue_id = jenkins_api.build_job(jenkins_job_name, parameters={'BRANCH': order_obj.branche})
        else:
            try:
                history = History.objects.get(pk=order_obj.content)
                build_number = history.jk_number
                queue_id = -1
            except:
                raise Exception('获取回滚版本失败')
        return build_number, queue_id


    def __get_steps(self, order_obj, deploy_path):
        minion = settings.DEPLOY.get('M_MINION')
        steps = ['init job', 'build', 'download package'] if order_obj.type != ROLLBACK else ['init job', 'download package']

        # 根据sls文件来获取步骤
        sls_file = os.path.join(deploy_path, order_obj.project.name, 'init.sls')
        cmd = "grep -o desc:.*$ {}|awk -F \"'\" '{{print $2}}'".format(sls_file)
        ret = saltapi.cmd_run(minion, arg=cmd)
        desc = ret['return'][0][minion]
        step_size = len(steps)+len(desc.split('\n'))*order_obj.project.servers.count()
        steps.extend(desc.split('\n'))

        return steps, step_size

    def init_deploy(self, cache_name, order_obj):
        deploy_path = settings.DEPLOY.get('CODE_PATH')
        jenkins_job_name = order_obj.project.jenkins_job
        deploy_cache = cache.get(cache_name, {})

        # 监测工单是否处于发布状态
        self.check_deploy(order_obj, deploy_cache)
        # 锁定上线
        cache.set(cache_name, {'is_lock': True}, timeout=CACHE_TIMEOUT)
        # 初始化jenkins
        build_number, queue_id = self.__init_jenkins(order_obj, jenkins_job_name)
        # 获取步骤
        steps, step_size = self.__get_steps(order_obj, deploy_path)

        deploy_cache = {
                          'job_name': order_obj.project.jenkins_job,
                          'status': S_RUNNING,
                          'build_number': build_number,
                          'is_lock': True,
                          'queue_id': queue_id,
                          'log': os.path.join(deploy_path, 'logs', str(time.time())),
                          'current_step': 1,
                          'step_size': step_size,
                          'steps': steps

                  }

        cache.set(cache_name, deploy_cache, timeout=CACHE_TIMEOUT)

        return build_number

    def start_deploy(self, cache_name, order_obj, assign_to):
        self.init_deploy(cache_name, order_obj)
        start_job(cache_name, order_obj, assign_to)
        # 设置发布状态
        update_obj(order_obj, status=D_RUNNING)


    def post(self, request, pk, format=None):
        order_obj = self.get_object()
        try:
            cache_name = 'deploy-{}'.format(order_obj.project.name)
            self.start_deploy(cache_name, order_obj, request.user.name)
        except DeployError as e:
            logger.exception(e)
            raise DeployError(e)
        except Exception as e:
            update_cache_value(cache_name, **{'is_lock': False, 'status': S_FAILED})
            logger.exception(e)
            return Response({'detail': '任务启动失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': '任务已启动'}, status=status.HTTP_200_OK)
        # return Response({
        #                     'project_name': order_obj.project.name,
        #                     'jenkins_job_name': jenkins_job_name,
        #                     'jenkins_build_number': jenkins_build_number,
        #                     'type': 'online'
        #                  })

    def get(self, request, pk, format=None):
        order_obj = self.get_object()
        cache_name = 'deploy-{}'.format(order_obj.project.name)
        data = cache.get(cache_name)
        return Response(data)


class RedeployJob(DeployJob):
    """
    重新上线
    """
    permission_classes = (permissions.IsAuthenticated, IsDevopsPermission)

    def check_deploy(self, order_obj, deploy_cache):
        # 结单大于12小时不能重新上线
        if order_obj.complete_time and (datetime.now() - order_obj.complete_time).total_seconds() > 12 * 3600:
            raise DeployError('超出重新上线的时间', 400)
        # 只有失败和成功状态的上线单才能重新上线
        elif order_obj.type == ROLLBACK or (order_obj.status != D_SUCCESSFUL and order_obj.status != D_FAILED):
            raise DeployError('该工单状态或类型不允许重新上线', 400)
        elif deploy_cache.get('is_lock'):
            raise DeployError('该任务已经启动')

    def start_deploy(self, cache_name, order_obj, assign_to):
        # 设置工单类型和状态
        # update_obj(order_obj, **{'status': D_PENDING, 'type': REONLONE})

        order_obj.type = REONLONE if order_obj.type != ROLLBACK else ROLLBACK
        super(RedeployJob, self).start_deploy(cache_name, order_obj, assign_to)

    def post(self, request, pk, format=None):
        order_obj = self.get_object()
        o_status = order_obj.status
        o_type = order_obj.type
        try:
            cache_name = 'deploy-{}'.format(order_obj.project.name)
            self.start_deploy(cache_name, order_obj, request.user.name)
        except DeployError as e:
            logger.exception(e)
            raise DeployError(e)
        except Exception as e:
            update_obj(order_obj, **{'status': o_status, 'type': o_type})
            update_cache_value(cache_name, **{'is_lock': False, 'status': S_FAILED})
            logger.exception(e)
            return Response({'detail': '任务启动失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': '任务已启动'}, status=status.HTTP_200_OK)


class DeployRealtimeLog(BaseDeployAPIView):
    """
    获取上线实时日志
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, pk, format=None):
        try:
            order_obj = self.get_object()
            cache_name = 'deploy-{}'.format(order_obj.project.name)
            deploy_cache = cache.get(cache_name, {})
            log_file = deploy_cache.get('log')
            lineno = int(request.GET.get('lineno', 1))

            if not deploy_cache:
                return Response({'detial': '找不到此工单的实时上线信息'}, status=status.HTTP_404_NOT_FOUND)

            linecache.clearcache()
            lines  = linecache.getlines(log_file)[lineno-1:]

            return Response(lines)
        except Exception as e:
            logger.exception(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SaltStateSLSWebhook(BaseDeployAPIView):
    """
    salt state.sls 回调地址,用于汇报当前发布执行到哪一步
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, pk, format=None):
        try:
            order_obj = self.get_object()
            cache_name = 'deploy-{}'.format(order_obj.project.name)
            deploy_cache = cache.get(cache_name)

            if not deploy_cache or not deploy_cache.get('is_lock'):
                raise Exception

            set_step_cache(cache_name, deploy_cache)

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Test(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        d = DeploymentOrder.objects.get(pk='b200965b-5f92-499b-86fc-bd24511e9ac2')
        logger.debug(d.title)
        logger.debug(d.project.servers_ip)
        return Response('OK', status=200)

    def post(self, request, format=None):
        # ret = saltapi.state_sls(['devops', None], **{
        #     'mods': 'devops-server',
        #     'saltenv': 'deploy'
        # })
        from common.utils import Bcolor
        print(Bcolor.red('start:{}'.format(time.time())))

        rets = saltapi.state_sls(['minion-1'], **{
            'pillar':
                {
                    'order_id':'ba74e384513f4f63b6643727444a8172',
                    'env': 2,
                    'devops_env': 'dev'
                },
            'mods': 'devops-server',
            'saltenv': 'deploy',

        })

        print(Bcolor.green(rets))


        return Response('lemon1913', status=200)

