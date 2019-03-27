__author__ = 'singo'
__datetime__ = '2019/3/18 2:24 PM '

from rest_framework import viewsets, permissions, mixins, generics, status
from rest_framework.response import Response
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from ..serializers import PermissionGroupSerializers, UserSerializer
from common.pagination import CustomPagination

User = get_user_model()

class GroupViewSet(viewsets.ModelViewSet):
    '''
    权限组管理

    get:
        获取权限组列表

    post:
        新建权限组

    patch/put:
        更新权限组

    delete:
        删除权限组
    '''
    lookup_field = 'pk'
    lookup_value_regex = '[0-9]+'
    serializer_class = PermissionGroupSerializers
    queryset = Group.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    pagination_class = CustomPagination
    search_fields = ('name',)

class GroupUsersViewset(viewsets.GenericViewSet):
    """
    权限组成员管理

    retrieve:
    返回指定组成员列表

    update:
    更新权限组成员

    destroy:
    清除权限组成员
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_field = 'pk'
    lookup_value_regex = '[0-9]+'

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        return generics.get_object_or_404(Group, **filter_kwargs)

    def get_queryset(self):
        group = self.get_object()
        return group.user_set.all()

    def retrieve(self, request, *args, **kwargs):
        '''
        返回指定组成员列表
        '''
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        '''
        更新用户组成员
        :param request.post:
                json:
            {
                "users": [user_id, ......],
                "reset":bool
            }
            reset默认值为True,当reset为True时重置权限组成员,当reset为True时添加权限组成员
        '''
        try:
            users = request.data.get('users', [])
            reset = request.data.get('reset', True)
            group = self.get_object()
            user_queryset = User.objects.filter(pk__in=users)
            if reset:
                group.user_set.set(user_queryset)
            else:
                group.user_set.add(*user_queryset)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': '权限组成员更新成功'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        '''
        清空用户组成员
        '''
        group = self.get_object()
        group.user_set.clear()
        return Response({'detail':'清除权限组成员成功'}, status=status.HTTP_204_NO_CONTENT)

class UserGroupsViewset(viewsets.GenericViewSet):
    '''
    用户权限组管理

    retrieve:
    返回指定用户所在权限组

    update:
    更新成员的权限组

    destroy:
    清空成员的权限组
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PermissionGroupSerializers
    lookup_field = 'pk'
    lookup_value_regex = '[0-9a-z\-]{32,36}'

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        return generics.get_object_or_404(User, **filter_kwargs)

    def get_queryset(self):
        user = self.get_object()
        return user.groups

    def retrieve(self, request, *args, **kwargs):
        '''
        返回指定用户所在权限组
        '''
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        '''
        更新用户的权限组
        :param request.post:
                json:
            {
                "groups": [group_id, ......],
                "reset":bool
            }
            reset默认值为True,当reset为True时重置权限组,当reset为True时添加权限组
        '''
        try:
            groups = request.data.get('groups', [])
            reset = request.data.get('reset', True)
            user = self.get_object()
            group_queryset = Group.objects.filter(pk__in=groups)
            if reset:
                user.groups.set(group_queryset)
            else:
                user.groups.add(*group_queryset)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': '更新权限组成功'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        '''
        清空权限组
        '''
        group = self.get_object()
        group.user_set.clear()
        return Response({'detail':'清除权限组成功'}, status=status.HTTP_204_NO_CONTENT)

