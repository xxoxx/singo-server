__author__ = 'singo'
__datetime__ = '2019/5/6 10:12 PM'


from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
from django.db.models import Q


from common.utils import logger
from common.permissions import DevopsPermission, DeployPermission, IsDevopsPermission
from common.pagination import CustomPagination
from ..serializers import DeploymentOrderSerializer, EnvServersMapSerializer
from ..filters import DeploymentOrderFilter
from ..models import DeploymentOrder, History
from ..common import *


class DeploymentOrderViewSet(viewsets.ModelViewSet):
    serializer_class = DeploymentOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = DeploymentOrderFilter
    search_fields = ('title', 'project__name')
    ordering_fields = ('apply_time',)
    pagination_class = CustomPagination
    queryset = DeploymentOrder.objects.all()

    def get_queryset(self):
        order_status = self.request.query_params.get('order_status')

        if self.request.user.is_superuser or self.request.user.is_devops:
            return DeploymentOrder.objects.all()
        # 返回进行中的上线单
        elif order_status == 'going':
            return DeploymentOrder.objects.filter((Q(applicant=self.request.user) |
                                                  Q(reviewer=self.request.user) |
                                                  Q(assign_to=self.request.user)) &
                                                  (Q(status=D_UNREVIEWED) |
                                                   Q(status=D_PENDING) |
                                                   Q(status=D_RUNNING)))
        else:
            return DeploymentOrder.objects.filter(Q(applicant=self.request.user) |
                                                  Q(reviewer=self.request.user)  |
                                                  Q(assign_to=self.request.user))

    def get_permissions(self):
        if self.action == 'partial_update':
            permission_classes  = [permissions.IsAuthenticated, IsDevopsPermission]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    # @action(detail=True, methods=['get'], name='deploy-env-servers', url_path='env-servers-map')
    # def deploy_env_tree(self, request, pk):
    #     '''
    #     获取允许发布的主机
    #     :param request:
    #     :param pk:
    #     :return:
    #     '''
    #     obj = self.get_object()
    #     env_code = request.GET.get('env_code')
    #
    #     if not env_code:
    #        return Response([])
    #
    #     print(obj.project.project_servers.all())
    #     queryset = obj.project.project_servers.all().filter(parent_env__code=env_code)
    #     serializer = EnvServersMapSerializer(queryset, many=True)
    #
    #     return Response(serializer.data)



class RollBackList(APIView):
    """
    获取回滚列表
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, project_name, format=None):
        try:
            size = settings.DEPLOY.get('ROLLBACK_SIZE', 1)
            # orders = DeploymentOrder.objects.filter(project__name=project_name,
            #                                         status=D_SUCCESSFUL,
            #                                         type=ONLINE)[0:size]

            orders = DeploymentOrder.objects.filter(project__name=project_name,
                                                    status=D_SUCCESSFUL).filter(~Q(type=ROLLBACK))[0:size]
            data = []
            for order in orders:
                try:
                    h = History.objects.get(order_id=order.id, deploy_times=order.deploy_times)
                    data.append(
                        {
                            'content': h.id,
                            'title': order.title,
                            'branche': order.branche,
                            'commit_id': order.commit_id,
                            'commit': order.commit,
                            'env': order.env
                        }
                    )
                except:
                    continue

            return Response(data)
        except Exception as e:
            logger.exception(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

