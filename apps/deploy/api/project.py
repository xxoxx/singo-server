__author__ = 'singo'
__datetime__ = '2019/4/26 4:33 PM '

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.utils import logger
from common.permissions import DevopsPermission
from common.pagination import CustomPagination
from ..serializers import ProjectSerializer
from ..models import Project



class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('name', 'gitlab_project')
    ordering_fields = ('name',)
    pagination_class = CustomPagination
    queryset = Project.objects.all()