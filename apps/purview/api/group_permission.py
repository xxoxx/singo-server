__author__ = 'singo'
__datetime__ = '2019/3/15 3:17 PM '

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework import permissions
from django.apps import apps
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action

from ..serializers import PermissionGroupSerializers
from common.utils import logger
from common.permissions import DevopsPermission, IsSuperuser

class GroupPermissionsViewset(viewsets.GenericViewSet):
    '''
    get:
        获取组权限列表
        默认返回中文格式的权限点列表:[app名字.权限点名称,...]
        指定escape=false返回:[appName.codename,....]

    put:
        设置组权限

    delete:
        删除指定APP,model下的所有权限点
    '''
    permission_classes = (permissions.IsAuthenticated, DevopsPermission)
    serializer_class = PermissionGroupSerializers
    queryset = Group.objects.all()
    lookup_field = 'pk'
    lookup_value_regex = '[0-9]+'

    perms_map = {
        'GET': [],
        'PUT': ['{}.group_permission_permission_set'],
        'PATCH': ['{}.group_permission_permission_set'],
        'DELETE': ['{}.group_permission_permission_delete']
    }

    def retrieve(self, request, *args, **kwargs):
        '''
        获取组权限点列表
        '''
        group = self.get_object()

        permissions = [{'node': '{}.{}'.format(p.content_type.app_label, p.codename),
                        'nodeName': '{}.{}'.format(apps.get_app_config(p.content_type.app_label).verbose_name, p.name)}
                       for p in group.permissions.all()
        ]

        return Response(permissions)

    def update(self, request, *args, **kwargs):
        '''
            :param request.data:
                {
                   "appName": "workOrder",
                   "modelName": "workorder",
                   "codenames": ["delete", "delete_workorder"],
                   "reset":bool
                }
            reset默认值为True,当reset为True时重置组权限,当reset为True时添加组权限
        '''
        group = self.get_object()
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
                # 获取组所有权限点
                permissions_all = group.permissions.all()
                # 排除包含当前模块的权限点
                permissions_exclude = permissions_all.exclude(content_type=content_type)
                group.permissions.set((permissions_exclude | permissions_set))
            else:
                group.permissions.add(*permissions_set)

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
        group = self.get_object()
        try:
            app_name = request.data.get('appName')
            app = apps.get_app_config(app_name)
            model = app.get_model(request.data.get('modelName'))
            content_type = ContentType.objects.get_for_model(model)

            # 权限组所有权限点
            permissions_all = group.permissions.all()
            # 过滤要删除的权限
            permissions = permissions_all.exclude(content_type=content_type)
            group.permissions.set(permissions)

        except Exception as e:
            logger.error(e)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': '删除权限点成功'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['delete'], name='group-permissions-clear',
            url_path='clear', **{'perms_map':{'DELETE': ['{}.group_permission_permission_set']}})
    def permissions_all(self, request, pk):
        group = self.get_object()
        group.permissions.clear()
        return Response({'detail': '清除权限完成'}, status=status.HTTP_204_NO_CONTENT)


class GroupPermissionsViewsetV2(viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, IsSuperuser)
    serializer_class = PermissionGroupSerializers
    queryset = Group.objects.all()
    lookup_field = 'pk'
    lookup_value_regex = '[0-9]+'

    # 只允许admin账户修改权限组权限
    # perms_map = {
    #     'PUT': ['{}.group_permission_permission_set'],
    #     'PATCH': ['{}.group_permission_permission_set'],
    # }

    def update(self, request, *args, **kwargs):
        '''
            :param request.data:
             [
                "users.add_user",
                "users.change_user",
                "users.delete_user"
            ]
        '''
        group = self.get_object()
        permissions = []
        try:
            for permission_node in request.data:
                permission_node = permission_node.split('.', 1)
                permission = Permission.objects.get(
                    content_type__app_label=permission_node[0],
                    codename=permission_node[1]
                )
                permissions.append(permission)
            group.permissions.set(permissions)
        except Exception as e:
            logger.error(e)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': '设置权限成功'}, status=status.HTTP_204_NO_CONTENT)




