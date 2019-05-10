__author__ = 'singo'
__datetime__ = '2019/5/6 10:12 PM'


from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.db.models import Q

from common.utils import logger
from common.permissions import DevopsPermission, DeployPermission
from common.pagination import CustomPagination
from ..serializers import DeploymentOrderSerializer
from ..filters import DeploymentOrderFilter
from ..models import DeploymentOrder
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
        elif order_status == 'going':
            return DeploymentOrder.objects.filter((Q(applicant=self.request.user) |
                                                  Q(reviewer=self.request.user) |
                                                  Q(assign_to=self.request.user)) &
                                                  (Q(status=UNREVIEWED) |
                                                   Q(status=STAY_ONLINE) |
                                                   Q(status=ONLINEING)))
        else:
            return DeploymentOrder.objects.filter(Q(applicant=self.request.user) |
                                                  Q(reviewer=self.request.user)  |
                                                  Q(assign_to=self.request.user))
    # def list(self, request, *args, **kwargs):
    #     super().list()

class RollBackList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, project_name, format=None):
        try:
            size = settings.DEPLOY.get('ROLLBACK_SIZE', 1)
            orders = DeploymentOrder.objects.filter(project__name=project_name, status=ONLINED)[0:size]
            data = [{
                        'title': order.title,
                        'branche':order.branche,
                        'commit_id': order.commit_id,
                        'commit': order.commit
                     }
                    for order in orders]

            return Response(data)
        except Exception as e:
            logger.exception(e)
            logger.error(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)