__author__ = 'singo'
__datetime__ = '2019/6/11 2:19 PM'

from rest_framework import viewsets, permissions, mixins, status, generics
from rest_framework.response import Response

from common.utils import logger
from ..models import EnvServersMap
from ..serializers import EnvServersMapSerializer
from common.pagination import CustomPagination
from ..filters import EnvServersMapFilter


class EnvServersMapViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EnvServersMapSerializer
    queryset = EnvServersMap.objects.all()
    pagination_class = CustomPagination
    filter_class = EnvServersMapFilter
    search_fields = ('name',)
    ordering_fields = ('id',)

    def list(self, request, *args, **kwargs):
        # 不需要分页
        if self.request.GET.get('all') == 'true':
            # 不可这行代码会去读取缓存中的数据,删掉的数据还能被返回
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return super(EnvServersMapViewSet, self).list(request, *args, **kwargs)


