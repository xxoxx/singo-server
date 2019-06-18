__author__ = 'singo'
__datetime__ = '2019/6/11 2:19 PM'

from rest_framework import viewsets, permissions, mixins, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from django.db.models.deletion import ProtectedError


from common.utils import logger
from ..models import DeployEnv
from ..serializers import DeployEnvSerializer
from common.pagination import CustomPagination
from ..filters import DeployEnvFilter




class DeployEnvViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DeployEnvSerializer
    queryset = DeployEnv.objects.all()
    pagination_class = CustomPagination
    filter_class = DeployEnvFilter
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

    def destroy(self, request, *args, **kwargs):
        try:
            return super(DeployEnvViewSet, self).destroy(request, *args, **kwargs)
        except ProtectedError:
            raise APIException(detail='请先删除其他关联', code=500)


    @action(detail=False, methods=['get'], name='deploy-env-tree',url_path='tree')
    def deploy_env_tree(self, request):
        '''
        获取部署环境树
        :param request:
        :return:
        '''
        data = []
        parents = DeployEnv.objects.filter(parent=None)

        for parent in parents:
            serializer = self.get_serializer(parent)
            d = serializer.data
            children = DeployEnv.objects.filter(parent=parent)

            try:
                d['children'] = self.get_serializer(children, many=True).data
            except Exception:
                d['children'] = []

            data.append(d)

        return Response(data)