__author__ = 'singo'
__datetime__ = '2019/4/26 4:33 PM '

from rest_framework import viewsets, permissions, mixins, status

from common.utils import logger
from common.permissions import DevopsPermission
from common.pagination import CustomPagination
from ..serializers import ProjectSerializer
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

