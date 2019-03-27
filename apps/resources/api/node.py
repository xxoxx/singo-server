__author__ = 'singo'
__datetime__ = '2019/1/10 2:10 PM '

import logging
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.serializers import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.transaction import atomic
from django.shortcuts import get_object_or_404


from resources.serializers.node import NodeSerializer, NodeAssetsSerializer
from resources.serializers.server import SaltServerSerializer as ServerSerializer
from ..models.node import Node
from ..models.common import Pots
from ..models.server import Server
from common.pagination import CustomPagination
from ..filters import NodeFilter

logger = logging.getLogger('devops')

class NodeRootViewSet(viewsets.ModelViewSet):
    '''
        根节点相应操作
        get: 返回所有根节点
        create: 创建根节点
        update: 更新根节点
        get(node tree)返回根节点树
    '''
    lookup_field = 'id'
    lookup_value_regex = '[a-z0-9\-]+'
    queryset = Node.get_root_brothers()
    serializer_class = NodeSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_class = NodeFilter

    def __check_name(self, request):
        try:
            name = request.data.get('name').upper()
        except AttributeError:
            logger.error('修改/创建根节点时传递参数为None')
            raise ValidationError({'detail': '参数name不能为空'})

        if name in [root.name for root in Node.get_root_brothers()]:
            raise ValidationError({'detail': '已存在根节点{}'.format(name)})

    def create(self, request, *args, **kwargs):
        self.__check_name(request)
        # self.request.POST._mutable = True
        data = {
            'name': request.data.get('name').upper(),
            'key': Node.get_next_root_key()
        }

        node = Node.objects.create(**data)
        # key 是只读字段调用super无法生效
        # node =  super(NodeRootVieSet, self).create(request, *args, **kwargs)
        serializer = NodeSerializer(node)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        self.__check_name(request)

        try:
            node_name = self.request.data.get('name').upper()
            instance = self.get_object()
            pots = Pots.objects.get(node_name=instance.name)
        except AttributeError:
            logger.error('修改根节点时传递参数为None')
            raise ValidationError({'detail': '参数name不能为空'})
        except Pots.DoesNotExist:
            logger.error('修改资产-节点表中未存在的根节点引发的失败')
            raise ValidationError({'detail': '未知的根节点{}'.format(instance.name)})

        # 根节点必须转换为大写
        self.request.POST._mutable = True
        self.request.data['name'] = node_name
        self.request.POST._mutable = False

        with atomic():
            # 修改资产-节点表
            pots.node_name = node_name
            pots.save()
            instance = super(NodeRootViewSet, self).update(request, *args, **kwargs)
        return instance

    def perform_destroy(self, instance):
        with atomic():
            try:
                pots = Pots.objects.get(node_name=instance.name)
                pots.delete()
            except:
                pass
            instance.delete()

    def get_tree(self, father):
        '''
        递归获取tree
        :param father:
        :return:
        '''
        data = []
        if father.children:
            for child in father.children:
                if child.children:
                    serializer = NodeSerializer(child).data
                    _data = self.get_tree(child)
                    serializer['children'] = _data
                    data.append(serializer)
                else:
                    serializer = NodeSerializer(child).data
                    serializer['children'] = []
                    data.append(serializer)
        else:
            if not father.is_root:
                serializer = NodeSerializer(father).data
                serializer['children'] = []
                data.append(serializer)

        if father.is_root:
            serializer = NodeSerializer(father).data
            serializer['children'] = data
            data = [serializer]

        return data

    @action(detail=False, methods=['get'], name='Node Tree',
            url_path='tree', )
    def tree(self, request):
        '''
        返回某个根节点下的所有成员
        :param request:
        '''
        data = {}
        resources_name = request.GET.get('resourcesName', None)

        try:
            # 资产-节点表获取根节点的名称
            pots = Pots.objects.get(resources_name__contains=resources_name)
            # 获取对应资产的根节点
            root = Node.objects.get(name__contains=pots.node_name)
            data = self.get_tree(root)
        except Pots.DoesNotExist:
            data = {'detail': '资产-节点表中不存在{}'.format(resources_name)}
        except Node.DoesNotExist:
            data = {'detail': '不存着根节点{}'.format(pots.node_name)}
        except Exception as e:
            logger.error(e)

        return Response(data)

class NodeChildAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''
    update: 修改子节点名称
    destroy: 删除节点及所有子节点
    retrieve: 节点详情
    '''
    lookup_field = 'pk'
    lookup_value_regex = '[a-z0-9\-]+'
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_object(self):
        obj = super().get_object()
        if obj.is_root:
            raise ValidationError({'detail': '不支持根节点操作'})
        return obj

    def perform_destroy(self, instance):
        with atomic():
            for child in instance.all_children:
                child.delete()
            instance.delete()

class NodeChildrenAPIView(generics.ListCreateAPIView,
                          generics.UpdateAPIView):
    '''
    post: 创建子节点
    lost: 子节点列表
    update: 移动子节点
    '''
    lookup_field = 'pk'
    lookup_value_regex = '[a-z0-9\-]+'
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    pagination_class = CustomPagination

    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk :
            return Node
        obj = get_object_or_404(Node, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        # pk = self.kwargs.get('pk')
        # instance = Node.objects.get(pk=pk)
        instance = self.get_object()
        queryset = instance.children

        return queryset

    def post(self, request, *args, **kwargs):
        if not request.data.get('name'):
            raise ValidationError({
                'detail': '必须指定节点名称'
            })
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        name = request.data.get('name')
        if name in [child.name for child in instance.children]:
            raise ValidationError({'detail': '已存着相同名称的节点'})
        node = instance.create_child(name=name)
        serializer = NodeSerializer(node)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        node_id = request.data.get('nodeId')
        if not node_id:
            raise ValidationError({
                'detail': '必须指定移动节点ID'
            })

        try:
            node = Node.objects.get(pk=node_id)
        except Exception as e:
            logger.error('移动节点是传入非法ID')
            raise ValidationError({
                'detail': '非法节点ID'
            })

        instance = self.get_object()
        # 判断是否存在同名的兄弟节点
        if instance.name in [child.name for child in instance.children]:
            raise ValidationError({'detail': '已存着相同名称的节点'})

        node.father=instance
        serializer = NodeSerializer(node)
        return Response(serializer.data)

class NodeAssetsApi(generics.CreateAPIView,
                    generics.RetrieveDestroyAPIView):
    '''
    post: 创建资产与节点的关联(add)
    put: 更新资产与节点的关联(delete, add)
    delele: 删除资产与节点的关联(delete)
    get: 获取节点下的所有资产
    '''
    lookup_field = 'pk'
    lookup_value_regex = '[a-z0-9\-]+'
    queryset = Node.objects.all()
    serializer_class = NodeAssetsSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    pagination_class = CustomPagination

    # def check_throttles(self, request):
    #     super().check_throttles(request)

    def create(self, request, *args, **kwargs):
        # 验证数据
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        related_name = serializer.data.get('related_name')
        resource_id_list = serializer.data.get('resource_id')
        # modleClass = eval(related_name.title())
        instance = self.get_object()

        try:
            # 获取与之关联的related的数据
            related = getattr(instance, related_name)
            related_id_list = [str(item.id) for item in related.all()]
            # 需要添加资产与原有资产的合集
            new_related_id_list = list(set(resource_id_list).union(set(related_id_list)))
            related.set(new_related_id_list)
        except AttributeError:
            raise ValidationError({'detail': '不存在的related_name: {}'.format(related_name)})
        except Exception as e:
            logger.critical(e)
            raise ValidationError({'detail':e})
        return Response(status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        try:
            # 获取某个节点下的资产必须传入与之关联的related_name值
            related_name = request.GET.get('related_name')
            if not related_name:
                return Response({'detail': 'related_name 不能为空'})

            instance = self.get_object()
            related = getattr(instance, related_name)
            # 获取related的Serializer
            relatedSerializer = eval(related_name.title()+'Serializer')
            response_data = []
            queryset = related.all()
            page = self.paginate_queryset(queryset)
            # 序列化related准备返回给客户端
            if page is not None:
                for obj in page:
                    serializer = relatedSerializer(obj)
                    response_data.append(serializer.data)
                return self.get_paginated_response(response_data)
            return Response(response_data)

        except AttributeError as e:
            print(e)
            raise ValidationError({'detail': '不存在的资源: {}'.format(related_name)})
        except Exception as e:
            logger.error(e)
            raise ValidationError({'detail': '未知异常'})

    def destroy(self, request, *args, **kwargs):
        # 验证数据
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        related_name = serializer.data.get('related_name')
        resource_id_list = serializer.data.get('resource_id')
        instance = self.get_object()

        try:
            # 获取与之关联的related数据
            related = getattr(instance, related_name)
            related_id_list =[str(item.id) for item in related.all()]
            # 差集
            new_related_id_list = list(set(related_id_list).difference(set(resource_id_list)))
            related.set(new_related_id_list)
        except AttributeError:
            raise ValidationError({'detail': '不存在的related_name: {}'.format(related_name)})
        except Exception as e:
            logger.critical(e)
            raise ValidationError({'detail': e})

        return Response(status=status.HTTP_200_OK, headers=headers)


