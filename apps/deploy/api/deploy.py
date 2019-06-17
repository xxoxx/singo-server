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

from common.utils import logger, update_cache_value, update_obj
from common.permissions import DevopsPermission, DeployPermission, IsDevopsPermission, ReDeployPermission
from ..models import DeploymentOrder
from common.apis import saltapi
from ..tasks import start_job, DeployJob
from ..common import *


class DeployAPI(object):
    def __init__(self, order_obj, login_user):
        self.order_obj = order_obj
        self.login_user = login_user
        self.cache_name = 'deploy-{}'.format(order_obj.project.name)

    def __init_deploy(self):
        deploy_path = settings.DEPLOY.get('CODE_PATH')
        deploy_cache = cache.get(self.cache_name, {})
        # 监测工单是否处于发布状态
        self.__check_deploy(self.order_obj, deploy_cache)
        # 锁定上线
        cache.set(self.cache_name, {'is_lock': True}, timeout=CACHE_TIMEOUT)
        # 获取步骤
        steps, step_size = self.__get_steps(self.order_obj, deploy_path)

        deploy_cache = {
                          'job_name': self.order_obj.project.jenkins_job,
                          'status': S_RUNNING,
                          'is_lock': True,
                          'log': os.path.join(deploy_path, 'logs', str(time.time())),
                          'current_step': 1,
                          'step_size': step_size,
                          'steps': steps
                  }

        cache.set(self.cache_name, deploy_cache, timeout=CACHE_TIMEOUT)

    # 检测是否在发布状态
    def __check_deploy(self, order_obj, deploy_cache):
        # 避免被重复执行部署
        if deploy_cache.get('is_lock'):
            raise DeployError('该任务已经启动')
        elif order_obj.status != 1:
            raise DeployError('该工单状态不能上线')
        return True

    # 获取发布步骤名称及步骤总数
    def __get_steps(self, order_obj, deploy_path):
        minion = settings.DEPLOY.get('M_MINION')
        steps = ['init job', 'build', 'download package'] if order_obj.type != ROLLBACK else ['init job', 'download package']
        # 根据sls文件来获取步骤
        sls_file = os.path.join(deploy_path, order_obj.project.name, 'init.sls')
        cmd = "grep -o desc:.*$ {}|awk -F \"'\" '{{print $2}}'".format(sls_file)
        ret = saltapi.cmd_run(minion, arg=cmd)
        desc = ret['return'][0][minion]
        step_size = len(steps)+len(desc.split('\n'))*len(order_obj.get_deploy_servers)
        steps.extend(desc.split('\n'))

        return steps, step_size

    def start_deploy(self):
        self.__init_deploy()
        start_job(self.cache_name, self.order_obj, self.login_user)
        # 设置发布状态
        update_obj(self.order_obj, status=D_RUNNING)

    def restart_deploy(self):
        self.order_obj.status = D_PENDING
        self.order_obj.type = REONLONE if self.order_obj.type != ROLLBACK else ROLLBACK
        self.start_deploy()
        # self.__init_deploy()
        # start_job(self.cache_name, self.order_obj, self.login_user)
        # # 设置发布状态
        # update_obj(self.order_obj, status=D_RUNNING)


class DeployError(APIException):
    status_code = 403
    default_detail = 'deploy error'
    default_code = 'invalid'


class BaseDeployAPIView(APIView):
    def get_object(self):
        obj = get_object_or_404(DeploymentOrder, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class DeployAPIView(BaseDeployAPIView):
    """
    项目上线

    post:
        启动上线

    get:
        获取上线状态
    """
    permission_classes = (permissions.IsAuthenticated, DeployPermission)

    def post(self, request, pk, format=None):
        order_obj = self.get_object()
        try:

            # cache_name = 'deploy-{}'.format(order_obj.project.name)
            # self.start_deploy(cache_name, order_obj, request.user.name)
            deploy = DeployAPI(order_obj, request.user.name)
            deploy.start_deploy()
        except DeployError as e:
            logger.exception(e)
            return Response({'detail': e.detail}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            update_cache_value(deploy.cache_name, **{'is_lock': False, 'status': S_FAILED})
            return Response({'detail': '任务启动失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': '任务已启动'}, status=status.HTTP_200_OK)

    def get(self, request, pk, format=None):
        order_obj = self.get_object()
        cache_name = 'deploy-{}'.format(order_obj.project.name)
        data = cache.get(cache_name)
        return Response(data)


class RedeployAPIView(DeployAPIView):
    """
    重新上线
    """
    permission_classes = (permissions.IsAuthenticated, IsDevopsPermission, ReDeployPermission)

    def post(self, request, pk, format=None):
        order_obj = self.get_object()
        o_status = order_obj.status
        o_type = order_obj.type
        try:
            deploy = DeployAPI(order_obj, request.user.name)
            deploy.restart_deploy()
        except DeployError as e:
            logger.exception(e)
            return Response({'detail': e.detail}, status=status.HTTP_200_OK)
        except Exception as e:
            update_obj(order_obj, **{'status': o_status, 'type': o_type})
            update_cache_value(deploy.cache_name, **{'is_lock': False, 'status': S_FAILED})
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

            DeployJob.set_step_cache(cache_name, deploy_cache)

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Test(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        saltapi.state_sls('devops', **{
            'pillar':
                {'project': 'devops-server',
                 'order_id': 'ba74e384-513f-4f63-b664-3727444a8172',
                 'env': 'test',
                 'devops_env': settings.ENV,
                 'private_vars': {'devops': {'xenv': '1111111'}}
                 },
            'mods': 'devops-server',
            'saltenv': 'deploy'
        })
        return Response('OK', status=200)


