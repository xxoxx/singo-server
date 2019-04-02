__author__ = 'singo'
__datetime__ = '2019/3/7 5:09 PM '

from rest_framework import permissions, viewsets, status, mixins, generics
from rest_framework.response import Response
from django.contrib.auth.models import Permission
from rest_framework.decorators import action
from django.apps import apps
from django.contrib.contenttypes.models import ContentType

from ..serializers import AuthPermissonSerializers, ContentTypeSerializers
from common.utils import logger
from common.permissions import DevopsPermission

def model_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

def get_apps():
    data = []
    for app in apps.get_app_configs():
        try:
            if app.is_purview:
                data.append(
                    {
                        'name': app.name,
                        'label': app.verbose_name
                    }
                )
        except:
            pass
    return data

def get_models(app_label):
    data = []
    app = apps.get_app_config(app_label)
    for name, model in app.models.items():
        try:
            if model._meta.is_purview:
                content_type = ContentType.objects.get_for_model(model)
                data.append(
                    {
                        'name': name,
                        'label': model._meta.verbose_name,
                        'content_type':
                            {
                                'id': content_type.id,
                                'model': content_type.model
                            }
                    }
                )
        except:
            pass
    return data

def get_permission_nodes(app_label, model_name, user=None, with_groups=False):
    data = []
    app = apps.get_app_config(app_label)
    model = app.get_model(model_name)
    if model._meta.is_purview:
        # queryset = get_perms_for_model(model)
        # content_type = ContentType.objects.get_for_model(model)
        # queryset = Permission.objects.filter(content_type=content_type)
        parms = {
            'content_type__app_label': app_label,
            'content_type__model': model_name
        }

        if user and user.is_superuser:
            pass
        elif user and with_groups:
            permissions = user.get_all_permissions()
            codename_list = [p.split('.')[1] for p in permissions]
            parms['codename__in'] = codename_list
        elif user:
            queryset = Permission.objects.filter(
                content_type__app_label=app_label,
                content_type__model=model_name)
            parms['user'] = user
        else:
            pass

        # permissions = user.get_all_permissions()
        # codename_list = [p.split('.')[1] for p in permissions]
        # queryset = Permission.objects.filter(codename__in=codename_list)
        # queryset = queryset.filter(
        #     content_type__app_label=app_label,
        #     content_type__model=model_name)

        queryset = Permission.objects.filter(**parms)
        serializer = AuthPermissonSerializers(queryset, many=True)
        data = serializer.data
    return data


class PermissonQueryViewSet(viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = AuthPermissonSerializers
    queryset = Permission.objects.all()
    lookup_field = 'pk'
    lookup_value_regex = '[a-z0-9\-]+'
    ordering_fields = ('id',)
    search_fields = ('name', 'codename')

    @action(detail=False, methods=['get'],
            name='permission-apps', url_path='apps')
    def apps(self, request):
        '''
        获取所有APP
        :param request:
        :return {"app":val, "label":val}:
        '''
        data = get_apps()
        return Response(data)

    @action(detail=False, methods=['get'],
            name='app-models', url_path='(?P<app>[a-zA-Z]+)/models')
    def modules(self, request, app):
        '''
        获取APP下所有model
        :return: {"model":val, "label":val}
        '''
        try:
            data = get_models(app)
        except Exception as e:
            return Response({'detail': '找不到应用名称'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data)

    @action(detail=False, methods=['get'], name='app-model-permissions',
            url_path='(?P<app>[a-zA-Z]+)/(?P<model>[a-zA-Z]+)/permissions')
    def permissions_node(self, request, app, model):
        '''
        获取模块权限点
        :return:
        {
            "id": val,
            "name": val,
            "codename": val,
            "content_type": val,
            "node": val
        },
        '''
        try:
            data = get_permission_nodes(app, model)
        except Exception as e:
            logger.error(e)
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)

        return Response(data)

    @action(detail=False, methods=['get'], name='permission-tree', url_path='permission-tree')
    def permissions_tree(self, request):
        '''
        获取权限树
        :param request:
        :return:
        '''
        try:
            apps = get_apps()
            for app in apps:
                app['models'] = get_models(app.get('name'))
                for model in app['models']:
                    model['permissions'] = get_permission_nodes(app.get('name'), model.get('name'))
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(apps)

    @action(detail=False, methods=['get'], name='permission-list', url_path='permission-list')
    def permissions_list(self, request):
        '''
        获取所有权限点列表
        '''
        # permissions = Permission.objects.all()
        # permissions = ['{}.{}'.format(p.content_type.app_label, p.codename) for p in permissions]
        # return Response(permissions)
        permissions = []
        try:
            apps = get_apps()
            for app in apps:
                app['models'] = get_models(app.get('name'))
                for model in app['models']:
                    queryset = Permission.objects.filter(
                        content_type__app_label=app.get('name'),
                        content_type__model=model.get('name'))
                    permissions += list(queryset)
            permissions = ['{}.{}'.format(permission.content_type.app_label, permission.codename) for permission in permissions]
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(permissions)

class AuthPermissonViewSet(mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    '''
    权限点管理

    post:
        新增权限点

    put:
        修改权限点

    delete:
        删除权限点

    '''

    serializer_class = AuthPermissonSerializers
    queryset = Permission.objects.all()
    permission_classes = (permissions.IsAuthenticated, DevopsPermission)
    lookup_field = 'pk'
    lookup_value_regex = '[0-9]+'
    perms_map = {
        'GET': [],
        'POST': ['{}.permission_add'],
        'PUT': ['{}.permission_edit'],
        'PATCH': ['{}.permission_edit'],
        'DELETE': ['{}.permission_delete']
    }

