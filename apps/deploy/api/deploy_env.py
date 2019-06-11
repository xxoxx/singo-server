__author__ = 'singo'
__datetime__ = '2019/6/11 2:19 PM'

from rest_framework import viewsets, permissions, mixins, status, generics
from rest_framework.response import Response

from common.utils import logger
from ..models import DeployEnv
from ..serializers import DeployEnvSerializer
from common.pagination import CustomPagination



class DeployEnvViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DeployEnvSerializer
    queryset = DeployEnv.objects.all()
    pagination_class = CustomPagination
    search_fields = ('name',)
    ordering_fields = ('id',)


    def list(self, request, *args, **kwargs):
        # 不需要分页
        if self.request.GET.get('all') == 'true':
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return super(DeployEnvViewSet, self).list(request, *args, **kwargs)