__author__ = 'singo'
__datetime__ = '2019/6/11 2:19 PM'

from rest_framework import viewsets, permissions, mixins, status, generics
from rest_framework.response import Response

from common.utils import logger
from ..models import DeployItem
from ..serializers import DeployItemSerializer
from common.pagination import CustomPagination
from ..filters import DeployItemFilter


class DeployItemViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DeployItemSerializer
    queryset = DeployItem.objects.all()
    pagination_class = CustomPagination
    filter_class = DeployItemFilter
    search_fields = ('name',)
    ordering_fields = ('id',)
