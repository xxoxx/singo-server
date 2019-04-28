__author__ = 'singo'
__datetime__ = '2019/4/28 10:42 AM '


from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.utils import logger
from common.permissions import DevopsPermission
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