import logging
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.db.transaction import atomic
from django.db.models import Q

from resources.serializers.server import ServerSerializer, SaltServerSerializer
from resources.serializers.pots import PotsSerializer
from resources.serializers.node import NodeSerializer
from ..models.server import Server
from ..models.node import Node
from ..models.common import Pots
from common.pagination import CustomPagination
from ..filters import ServerFilter



logger = logging.getLogger('devops')

class ServerViewSet(viewsets.ModelViewSet):
    # queryset = Server.objects.all()
    serializer_class = ServerSerializer
    list_serializer_class = SaltServerSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, IsAdminUser)
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
        resources_name = Server.__name__.upper()
        node_name = request.data.get('name').upper()

        if not node_name:
            logger.error('创建根节点不能指定空值')
            raise ValidationError({'detail': '创建节根点失败'})
        elif node_name in [root.name for root in Node.get_root_brothers()]:
            raise ValidationError({'detail': '已存在根节点{}'.format(node_name)})
        else:
            with atomic():
                pots, created = Pots.objects.update_or_create(resources_name=resources_name)
                pots.node_name = node_name
                pots.save()

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
        from common.saltapi import saltapi
        import ast
        from common.utils import Bcolor
        server = self.get_object()
        #
        # time.sleep(10)
        # return Response({'ok':'ok'})

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
        except KeyError:
            status = 500
            response = {'detail': 'KeyError'}
            logger.error('KeyError')
        except Exception as e:
            response = {'detail': str(e)}
            logger.error(e)
            status = 500

        return Response(response, status=status)
