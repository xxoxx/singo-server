__author__ = 'singo'
__datetime__ = '2019/4/26 4:33 PM '

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action

from common.utils import logger
from common.permissions import DevopsPermission
from common.pagination import CustomPagination
from ..serializers import ProjectSerializer, EnvServersMapSerializer
from ..models import Project, History



class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('name', 'gitlab_project')
    ordering_fields = ('name',)
    pagination_class = CustomPagination
    queryset = Project.objects.all()

    # 更新name的时候还需要考虑history,不然不便于统计
    def perform_update(self, serializer):
        obj = self.get_object()
        serializer.save()

        try:
            new_name = serializer.data.get('name')

            if new_name != obj.name:
                History.objects.filter(project_name=obj.name).update(project_name=new_name)
        except Exception as e:
            logger.exception(e)
            logger.warning(e)


    @action(detail=True, methods=['get'], name='env-servers-map', url_path='env-servers-map')
    def deploy_env_tree(self, request, pk):
        '''
        获取允许发布的主机
        :param request:
        :param pk:
        :return:
        '''
        obj = self.get_object()
        env_code = request.GET.get('env_code')

        if not env_code:
           return Response([])

        queryset = obj.project_servers.all().filter(parent_env__code=env_code)
        serializer = EnvServersMapSerializer(queryset, many=True)

        return Response(serializer.data)

