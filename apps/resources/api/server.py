from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.db.transaction import atomic

from resources.serializers.server import ServerSerializer, SaltServerSerializer
from resources.serializers.pots import PotsSerializer
from resources.serializers.node import NodeSerializer
from ..models.server import Server
from ..models.node import Node
from common.pagination import CustomPagination
from ..filters import ServerFilter
from common.utils import logger
from common.permissions import IsSuperuser
from ..createSources.server import saveServer
from common.apis import saltapi

class ServerViewSet(viewsets.ModelViewSet):
    '''
    主机管理

    get:
        获取主机列表

    post:
        手动添加主机

    put/patch:
        更新主机信息

    delete:
        删除主机

    get(detail):
        获取主机详情
    '''
    serializer_class = ServerSerializer
    list_serializer_class = SaltServerSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, IsSuperuser)
    queryset = Server.objects.all()
    filter_class = ServerFilter
    ordering_fields = ('hostname', 'created')
    search_fields = ('hostname', 'saltID', 'innerIpAddress__ip', 'publicIpAddress__ip')

    def get_serializer_class(self):
        if self.action in['retrieve', 'list']:
            if hasattr(self, 'list_serializer_class'):
                return self.list_serializer_class

        return super(ServerViewSet, self).get_serializer_class()

    # def get_queryset(self):
    #     node_id = self.request.GET.get('node_id')
    #     print(node_id)
    #     # 为node添加主机时需要过滤已经拥有的主机
    #     if node_id:
    #         return Server.objects.filter(~Q(nodes__id=node_id))
    #     return Server.objects.all()

    # 创建资源与节点的关联, 只能在这里创建最合适不然资源名字无法设置唯一
    @action(detail=False, methods=['post'], name='Pots', url_path='pots',
            serializer_class=PotsSerializer)
    def create_pots(self, request, *args, **kwargs):
        resources_name = Server.__name__.upper()+'S'
        node_name = request.data.get('node_name').upper()

        serializer = self.get_serializer(data = {
                                    'resources_name': resources_name,
                                    'node_name': node_name
                                    })
        serializer.is_valid(raise_exception=True)

        if node_name in [root.name for root in Node.get_root_brothers()]:
            raise ValidationError({'detail': '已存在根节点{}'.format(node_name)})
        else:
            with atomic():
                serializer.save()
                # 设置资产的根节点
                data = {
                    'name': node_name,
                    'key': Node.get_next_root_key()
                }
                node = Node.objects.create(**data)
                # 返回创建成功后的序列化数值
                serializer = NodeSerializer(node)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'], name='system-info', url_path='system-info')
    def get_system_info(self, request, pk=None):
        from common.apis.saltapi import saltapi
        import ast

        server = self.get_object()

        if not server.saltID:
            logger.error('无法获取系统信息,salt未指定')
            response = {'detail': '无法获取系统信息,salt未指定'}
            return Response(response, status=500)
        # 通过脚本获取系统信息
        req = saltapi.run_script(server.saltID, 'scripts/python/get_system_info.py')

        try:
            response = req[0][server.saltID]['stdout']
            response = ast.literal_eval(response)
            status = 200
        except Exception as e:
            response = {'detail': str(e)}
            logger.error(e)
            status = 500

        return Response(response, status=status)


class SaltServerViewSet(viewsets.GenericViewSet):
    serializer_class = SaltServerSerializer
    permission_classes = (IsAuthenticated, IsSuperuser)

    def create(self, request, *args, **kwargs):
        salt_id = request.data.get('keyID')
        data = saltapi.get_grains_items(salt_id)

        try:
            if data['code'] == 200:
                data['comment'] = '来自salt添加'
                response = saveServer(data)
                status = 201
            else:
                response = {'detail': '获取salt资产信息失败'}
                status = 500
        except ValidationError as e:
            logger.error(e)
            response = {'detail': '资产中已存在此saltID的资产'}
            status = 500
        except Exception as e:
            logger.error(e)
            response = {'detail': '添加资产失败'}
            status = 500

        return Response(data=response, status=status)