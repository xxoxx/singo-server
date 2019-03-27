import django_filters
from .models.server import Server
from .models.node import Node


class ServerFilter(django_filters.rest_framework.FilterSet):
    '''
    主机过滤
    '''
    hostname = django_filters.CharFilter(lookup_expr='icontains')
    provider = django_filters.CharFilter(field_name='provider__name', lookup_expr='icontains')
    innerIpAddress = django_filters.CharFilter(field_name='innerIpAddress__ip', lookup_expr='icontains')
    publicIpAddress = django_filters.CharFilter(field_name='publicIpAddress__ip', lookup_expr='icontains')
    nodeId = django_filters.UUIDFilter(field_name='nodes__id')
    nodeId_except = django_filters.UUIDFilter(field_name='nodes__id', exclude=True)



    class Meta:
        model = Server
        fields = ['hostname', 'innerIpAddress', 'publicIpAddress',
                  'provider', 'nodeId', 'nodeId_except']

class NodeFilter(django_filters.rest_framework.FilterSet):
    '''
    节点过滤
    '''
    name = django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = Node
        fields = ['name']
