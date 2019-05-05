__author__ = 'singo'
__datetime__ = '2019/5/5 10:44 AM '


from rest_framework import viewsets, permissions, mixins, status


class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = DeploymentOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = DeploymentOrderFilter
    search_fields = ('title', 'project')
    ordering_fields = ('start',)
    pagination_class = CustomPagination
    queryset = DeploymentOrder.objects.all()