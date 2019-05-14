from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from ..models import UserGroup
from ..models.user import User
from ..serializers import UserGroupSerializer, UserSerializer
from common.pagination import CustomPagination
from common.utils import logger
from common.permissions import DevopsPermission

class UserGroupleViewSet(viewsets.ModelViewSet):
    '''
    用户组管理

    get:
        获取用户列表

    post:
        创建用户组

    put/patch:
        更新用户组

    delete:
        删除用户组
    '''
    lookup_field = 'pk'
    lookup_value_regex = '[a-z0-9\-]+'
    serializer_class = UserGroupSerializer
    permission_classes = (permissions.IsAuthenticated, DevopsPermission)
    pagination_class = CustomPagination
    search_fields = ('name',)
    queryset = UserGroup.objects.all()

    perms_map = {
        'GET': [],   # 这里受限制会导致用户信息无法获取用户组
        'POST': ['{}.user_group_add'],
        'PUT': ['{}.user_group_edit'],
        'PATCH': ['{}.user_group_edit'],
        'DELETE':['{}.user_group_delete']
    }

    @action(detail=False, methods=['get'], name='group-devops',
            url_path='devops', permission_classes=[permissions.IsAuthenticated])
    def get_devops_members(self, request):
        '''
        获取运维组成员
        '''
        try:
            group = UserGroup.objects.get(name='devops')
            members = group.members.all()
            serializer = UserSerializer(members, many=True)
        except Exception as e:
            # 不存着devops组就获取超级用户
            members = User.objects.filter(is_superuser=1)
            serializer = UserSerializer(members, many=True)
            logger.error('获取运维组失败!')

        return Response(serializer.data)



