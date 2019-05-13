__author__ = 'singo'
__datetime__ = '2019/4/28 10:42 AM'


from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django.conf import settings
import os, time, linecache


from common.utils import logger
from common.permissions import DevopsPermission, DeployPermission
from common.pagination import CustomPagination
from rest_framework.decorators import action
from ..serializers import DeploymentOrderSerializer
from ..models import DeploymentOrder
from ..filters import DeploymentOrderFilter
from common.apis import jenkins_api, saltapi
from ..tasks import start_job
from ..common import *
from ..models import History




class DeployJob(APIView):
    permission_classes = (permissions.IsAuthenticated, DeployPermission)

    def get_object(self):
        obj = get_object_or_404(DeploymentOrder, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj

    def __init_deploy(self, cache_name, order_obj):
        deploy_path = settings.DEPLOY.get('CODE_PATH')
        minion = settings.DEPLOY.get('M_MINION')
        jenkins_job_name = order_obj.project.jenkins_job

        if order_obj.type == ONLINE:
            # 启动jenkins构建
            # next_build_number = jenkins_api.get_next_build_number(jenkins_job_name)
            # queue_id = jenkins_api.build_job(jenkins_job_name, parameters={'BRANCH': order_obj.branche})
            next_build_number = 1
            queue_id = 1
            steps = ['initJob','build', 'downloadPackage']
        else:
            try:
                history = History.objects.get(pk=order_obj.content)
                next_build_number = history.jk_number
                queue_id = -1
            except:
                raise Exception('获取回滚版本失败')

            steps = ['initJob', 'downloadPackage']

        # 更加sls文件来获取步骤
        try:
            sls_file = os.path.join(deploy_path, order_obj.project.name, 'init.sls')
            cmd = "grep -o desc.*$ {}|awk -F '=' '{{print $2}}'".format(sls_file)
            ret = saltapi.cmd_run(minion, arg=cmd)
            desc = ret['return'][0][minion]
            steps.extend(desc.split('\n'))
        except Exception as e:
            logger.exception(e)

        deploy_cache = {
                          'job_name': order_obj.project.jenkins_job,
                          'build_number': next_build_number,
                          'is_lock': True,
                          'queue_id': queue_id,
                          'log': os.path.join(deploy_path, 'logs', str(time.time())),
                          'current_step': 1,
                          'steps': steps
                  }

        cache.set(cache_name, deploy_cache, timeout=24*3600)

        return next_build_number

    def post(self, request, pk, format=None):
        order_obj = self.get_object()
        try:
            jenkins_job_name = order_obj.project.jenkins_job
            cache_name = 'deploy-{}'.format(order_obj.project.name)
            deploy_cache = cache.get(cache_name, {})

            # 避免被重复执行部署
            if deploy_cache.get('is_lock'):
                raise DeployError('该任务已经启动')
            elif order_obj.status != 1:
                raise DeployError('该工单状态不能上线')
            else:
                # 锁定上线
                cache.set(cache_name, {'is_lock': True}, timeout=24*3600)

            # 初始化
            jenkins_build_number = self.__init_deploy(cache_name, order_obj)
            #启动任务
            # start_job(cache_name, order_obj)

            # 上线中
            order_obj.status = ONLINEING
            order_obj.save()

        except DeployError as e:
            logger.exception(e)
            raise DeployError(e)
        except Exception as e:
            cache.delete(cache_name)
            logger.exception(e)
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
                            'project_name': order_obj.project.name,
                            'jenkins_job_name': jenkins_job_name,
                            'jenkins_build_number': jenkins_build_number
                         })

    def get(self, request, pk, format=None):
        data = cache.get('deploy-devops-server')
        cache.delete('deploy-devops-server')
        return Response(data)

class DeployRealtimeLog(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self):
        obj = get_object_or_404(DeploymentOrder, pk=self.kwargs.get('pk'))
        # self.check_object_permissions(self.request, obj)
        return obj

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

class Test(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        # cmd = 'grep -Fc api/deploy /srv/salt/deploy/devops-server/init.sls'
        # ret = saltapi.cmd_run('devops', arg=cmd)
        print(request.GET.get('desc'))

        return Response('lemon1912', status=200)

    def post(self, request, format=None):
        ret = saltapi.state_sls(['devops', None], **{
            'mods': 'devops-server',
            'saltenv': 'deploy'
        })
        # saltapi.remote_state()
        print(ret)
        return Response('lemon1913', status=200)


from rest_framework.exceptions import APIException

class DeployError(APIException):
    status_code = 403
    default_detail = 'deploy error'
    default_code = 'invalid'