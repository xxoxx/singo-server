__author__ = 'singo'
__datetime__ = '2019/3/15 3:17 PM '

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework import permissions
from django.apps import apps
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action

from django.contrib.auth import get_user_model
from common.utils import Bcolor
from ..serializers import UserSerializer
from common.utils import logger
from common.permissions import DevopsPermission, IsSuperuser
from .permission_query import get_apps, get_models, get_permission_nodes
from common.permissions import DevopsPermission

User = get_user_model()

class UserPermissionsViewSet(viewsets.GenericViewSet):
    '''
        get:

            /detail/:获取用户所有APP权限点(不包括所在组)

            /detail/all/:获取用户所有APP权限点(包括

        put:
            设置用户权限(必须指定APP,model,permission node)
    '''
    permission_classes = (permissions.IsAuthenticated, DevopsPermission)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'
    lookup_value_regex = '[a-z0-9\-]{32,36}'

    perms_map = {
        'GET': [],
        'PUT': ['{}.{}.user_permission_set'],
        'PATCH': ['{}.{}.user_permission_set'],
        'DELETE': ['{}.user_permission_set']
    }

    def retrieve(self, request, *args, **kwargs):
        '''
        获取用户所有APP权限点(不包括所在组)
        [
            "purview.group_permission",
            ......
        ]
        '''
        user = self.get_object()
        permissions_all = ['{}.{}'.format(p.content_type.app_label, p.codename)
                       for p in Permission.objects.filter(user=user)]
        return Response(permissions_all)

    def update(self, request, *args, **kwargs):
        '''
            修改用户指定APP,model下的权限点
            :param request.data:
                {
                   "appName": "workOrder",
                   "modelName": "workorder",
                   "codenames": ["delete", "delete_workorder"],
                   "reset":bool
                }
                reset默认值为True,当reset为True时重置组权限,当reset为True时添加用户权限
        '''
        user = self.get_object()

        if user == request.user:
            return Response({'detail': '权限拒绝'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            app_name = request.data.get('appName')
            codenames = request.data.get('codenames')
            reset = request.data.get('reset', True)

            app = apps.get_app_config(app_name)
            model = app.get_model(request.data.get('modelName'))
            content_type = ContentType.objects.get_for_model(model)

            # 需要设置的权限点
            permissions_set = Permission.objects.filter(content_type=content_type, codename__in=codenames)

            if reset:
                # 用户所有权限点
                permissions_all = Permission.objects.filter(user=user)
                # 排除包含当前模块的权限点
                permissions_exclude = permissions_all.exclude(content_type=content_type)
                user.user_permissions.set((permissions_exclude | permissions_set))
            else:
                user.user_permissions.add(*permissions_set)

        except Exception as e:
            logger.error(e)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail':'权限设置成功'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        '''
        删除指定APP,model下的所有权限点
            :param request.data: {
                                   "appName": "workOrder",
                                   "modelName": "workorder",
                                }
        '''
        user = self.get_object()
        try:
            app_name = request.data.get('appName')
            app = apps.get_app_config(app_name)
            model = app.get_model(request.data.get('modelName'))
            content_type = ContentType.objects.get_for_model(model)

            # 用户所有权限点
            permissions = Permission.objects.filter(user=user)
            # 过滤要删除的权限
            permissions = permissions.exclude(content_type=content_type)
            user.user_permissions.set(permissions)

        except Exception as e:
            logger.error(e)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': '删除权限点成功'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get', 'delete'],
            name='user-permissions-all', url_path='all',
            **{'perms_map': {'GET':[], 'DELETE': ['{}.user_permission_set']}}
            )
    def permissions_all(self, request, pk):
        '''
        get:
            获取用户所有APP权限点(包括所在组)

        delete:
            删除用户所有权限点(无关组)
        '''
        user = self.get_object()
        if request.method == 'GET':
            permissions = user.get_all_permissions()
            return Response(permissions, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            user.user_permissions.clear()
            return Response({'detail': '清除权限完成'}, status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], name='user-permissions-tree',
            url_path='permission-tree', **{'perms_map': {'GET':[]}})
    def permissions_tree(self, request, pk):
        '''
        获取用户权限树
        :param request:
        :return:
        '''
        try:
            user = request.user
            apps = get_apps()
            for app in apps:
                app['models'] = get_models(app.get('name'))
                for model in app['models']:
                    model['permissions'] = get_permission_nodes(app.get('name'), model.get('name'), user=user, with_groups=True)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(apps)


class UserPermissionsViewSetV2(viewsets.GenericViewSet):
    '''
    更新用户权限点
    '''
    permission_classes = (permissions.IsAuthenticated, DevopsPermission)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'
    lookup_value_regex = '[a-z0-9\-]{32,36}'

    perms_map = {
        'PUT':['{}.user_permission_set'],
        'PATCH':['{}.user_permission_set'],
    }

    def update(self, request, *args, **kwargs):
        '''
            修改用户权限点
            :param request.data:
            [
                "users.add_user",
                "users.change_user",
                "users.delete_user"
            ]
        '''
        permissions = []
        user = self.get_object()

        # 不能自己给自己设置权限
        if user == request.user:
            return Response({'detail':'权限拒绝'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            for permission_node in request.data:
                permission_node = permission_node.split('.', 1)
                permission = Permission.objects.get(
                    content_type__app_label=permission_node[0],
                    codename=permission_node[1]
                )
                permissions.append(permission)
            user.user_permissions.set(permissions)
        except Exception as e:
            logger.error(e)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': '设置权限成功'}, status=status.HTTP_204_NO_CONTENT)
