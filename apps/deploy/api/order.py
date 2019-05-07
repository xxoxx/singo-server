__author__ = 'singo'
__datetime__ = '2019/5/6 10:12 PM'


from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView

from common.utils import logger
from common.permissions import DevopsPermission, DeployPermission
from common.pagination import CustomPagination
from ..serializers import DeploymentOrderSerializer
from ..models import DeploymentOrder
from ..filters import DeploymentOrderFilter




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