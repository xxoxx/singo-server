__author__ = 'singo'
__datetime__ = '2019/5/5 10:44 AM '


from rest_framework import viewsets, permissions, mixins, status

from ..serializers import HistorySerializer
from ..models import History
from common.pagination import CustomPagination

class HistoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = HistorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    # filter_class = DeploymentOrderFilter
    search_fields = ('title', 'project_name')
    ordering_fields = ('start',)
    pagination_class = CustomPagination
    queryset = History.objects.all()