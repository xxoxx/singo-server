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
from ..serializers import DeploymentOrderSerializer
from ..models import DeploymentOrder
from ..filters import DeploymentOrderFilter
from common.apis import jenkins_api, saltapi
from ..tasks import start_job, test
from ..common import *




class DeployJob(APIView):
    permission_classes = (permissions.IsAuthenticated, DeployPermission)

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        pk = filter_kwargs.get('pk')
        # pk = self.kwargs["pk"]
        obj = get_object_or_404(DeploymentOrder, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def __init_deploy_cache(self, build_number, queue_id, cache_name, order_obj):
        deploy_path = settings.DEPLOY.get('CODE_PATH')
        minion = settings.DEPLOY.get('M_MINION')

        if order_obj.type == ONLINE:
            steps = ['初始化','构建', '下载代码包']
        else:
            steps = ['初始化', '下载代码包']

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
                          'build_number': build_number,
                          'is_lock': True,
                          'queue_id': queue_id,
                          'log': os.path.join(deploy_path, 'logs', str(time.time())),
                          'current_step': 1,
                          'steps': steps
                  }


        cache.set(cache_name, deploy_cache, timeout=24*3600)


    def post(self, request, pk, format=None):
        order_obj = self.get_object()
        try:
            name = order_obj.project.jenkins_job
            cache_name = 'deploy-{}'.format(order_obj.project.name)
            deploy_cache = cache.get(cache_name, {})
            deploy_path = settings.DEPLOY.get('CODE_PATH')

            # 避免被重复执行部署
            if deploy_cache.get('is_lock'):
                raise DeployError('该任务已经启动')
            elif order_obj.status != 1:
                raise DeployError('该工单状态不能上线')
            else:
                # 锁定上线
                cache.set(cache_name, {'is_lock': True}, timeout=24*3600)

            # 启动jenkins构建
            next_build_number = jenkins_api.get_next_build_number(name)
            queue_id = jenkins_api.build_job(name, parameters={'BRANCH': order_obj.branche})
            # 初始化缓存
            self.__init_deploy_cache(next_build_number, queue_id, cache_name, order_obj)
            # deploy_cache = {
            #                   'job_name': name,
            #                   'build_number': next_build_number,
            #                   'is_lock': True,
            #                   'queue_id': queue_id,
            #                   'log': os.path.join(deploy_path, 'logs', str(time.time())),
            #                   'current_step': 1,
            #                   'steps': -1,
            #                   'label': '初始化'
            #           }
            #
            # cache.set(cache_name, deploy_cache, timeout=24*3600)
            #
            # 根据sls回调来判断总步骤数
            # try:
            #     minion = settings.DEPLOY.get('M_MINION')
            #     sls_file = os.path.join(deploy_path, order_obj.project.name, 'init.sls')
            #     cmd = 'grep -Fc api/deploy {}'.format(sls_file)
            #     ret = saltapi.cmd_run(minion, arg=cmd)
            #     steps = int(ret['return'][0][minion])
            #     deploy_cache['steps'] = steps + 3
            #     cache.set(cache_name, deploy_cache, timeout=24*3600)
            # except:
            #     pass

            # 异步
            start_job(cache_name, order_obj)

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
                            'jenkins_job_name': name,
                            'jenkins_build_number': next_build_number
                         })

    def get(self, request, pk, format=None):
        data = cache.get('deploy-devops-server')
        cache.delete('deploy-devops-server')
        return Response(data)

class DeployRealtimeLog(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(DeploymentOrder, pk=filter_kwargs.get('pk'))
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
        cmd = 'grep -Fc api/deploy /srv/salt/deploy/devops-server/init.sls'
        ret = saltapi.cmd_run('devops', arg=cmd)
        # print(request.GET.get('desc'))
        return Response('lemon1912', status=200)

from rest_framework.exceptions import APIException

class DeployError(APIException):
    status_code = 403
    default_detail = 'deploy error'
    default_code = 'invalid'