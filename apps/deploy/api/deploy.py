__author__ = 'singo'
__datetime__ = '2019/4/28 10:42 AM '


from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from django.conf import settings
import os, time


from common.utils import logger
from common.permissions import DevopsPermission, DeployPermission
from common.pagination import CustomPagination
from ..serializers import DeploymentOrderSerializer
from ..models import DeploymentOrder
from ..filters import DeploymentOrderFilter
from common.apis import jenkins_api, saltapi
from ..tasks import start_job


class DeploymentOrderViewSet(viewsets.ModelViewSet):
    serializer_class = DeploymentOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = DeploymentOrderFilter
    search_fields = ('title', 'project')
    ordering_fields = ('apply_time',)
    pagination_class = CustomPagination
    queryset = DeploymentOrder.objects.all()

    def get_queryset(self):
        if self.request.user.is_superuser:
            return DeploymentOrder.objects.all()
        else:
            return DeploymentOrder.objects.filter(applicant=self.request.user)


class DeployJob(APIView):
    permission_classes = (permissions.IsAuthenticated, DeployPermission)

    def get_object(self):
        obj = get_object_or_404(DeploymentOrder, pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk, format=None):
        order_obj = self.get_object()
        try:
            # cache.delete(obj.project.name)
            name = order_obj.project.jenkins_job
            cache_name = 'deploy-{}'.format(order_obj.project.name)
            deploy_cache = cache.get(order_obj.project.name, {})
            deploy_path = settings.DEPLOY.get('CODE_PATH')

            # 避免被重复执行部署
            if deploy_cache.get('is_lock'):
                raise DeployError('该任务已经启动')
            elif order_obj.status != 1:
                raise DeployError('该工单状态不能上线')

            # 上线中
            order_obj.status = 2
            order_obj.save()

            # 启动jenkins构建
            next_build_number = jenkins_api.get_next_build_number(name)
            queue_id = jenkins_api.build_job(name, parameters={'BRANCH': order_obj.branche})
            deploy_cache = {
                              'job_name': name,
                              'build_number': next_build_number,
                              'is_lock': True,
                              'queue_id': queue_id,
                              'log': os.path.join(deploy_path, 'logs', str(time.time())),
                              'current_step': 1,
                              'steps': -1,
                              'label': '初始化'
                      }

            cache.set(cache_name, deploy_cache, timeout=3600)

            # 根据sls回调来判断总步骤数
            try:
                minion = settings.DEPLOY.get('M_MINION')
                sls_file = os.path.join(deploy_path, order_obj.project.name, 'init.sls')
                cmd = 'grep -Fc api/deploy {}'.format(sls_file)
                ret = saltapi.cmd_run(minion, arg=cmd)
                steps = int(ret['return'][0][minion])
                deploy_cache['steps'] = steps + 3
                cache.set(cache_name, deploy_cache, timeout=3600)
            except:
                pass

            # 异步
            start_job(cache_name, order_obj)

        except DeployError as e:
            logger.exception(e)
            raise DeployError(e)
        except Exception as e:
            # isinstance(e, DeployError)
            logger.exception(e)
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
                            'project_name': order_obj.project.name,
                            'jenkins_job_name': name,
                            'jenkins_build_number': next_build_number
                         })

    def get(self, request, pk, format=None):
        data = cache.get('deploy-devops-server')
        return Response(data)


class Test(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        from ..models import History
        import datetime
        obj = History.objects.create(
            **{
                'servers_ip': '127.0.0.1',
                'servers_saltID':'devops',
                'branche': '123',
                'commit_id': '123456',
                'commit': 'commit',
                'jk_number': 1,
                'applicant': 'test',
                'reviewer': 'test',
                'assign_to': 'test',
                'result': 0,
                'log': '/temp'
            }
        )
        # obj = History.objects.get(pk=1)
        # obj.__dict__.update({'commit_id': '654321'})
        # obj.save()
        return Response('lemon1912', status=200)

from rest_framework.exceptions import APIException

class DeployError(APIException):
    status_code = 403
    default_detail = 'deploy error'
    default_code = 'invalid'