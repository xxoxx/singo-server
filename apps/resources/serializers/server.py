from rest_framework import serializers

from resources.models.server import Server
from resources.models.node import Node
from resources.models.common import Provider, Ip, Ram
from common.utils import init_kwargs

from .node import NodeSerializer

class ServerSerializer(serializers.Serializer):
    '''
    用户手动添加服务器使用的Serializer
    '''

    hostname = serializers.CharField(max_length=128, label='主机名')
    provider = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(),
                                                  many=False, label='供应商')
    # provider_name = serializers.SerializerMethodField()
    saltID = serializers.CharField(max_length=128, label='saltID', allow_null=True)
    # planform = serializers.ChoiceField(choices=['Linux', 'Windows', 'Solaris', 'Unknow'], label='平台')
    env = serializers.ChoiceField(choices=Server.ENV, label='环境')
    _IP = serializers.IPAddressField(label='连接IP', allow_null=True)
    # protocol = serializers.CharField(choices=['ssh'], label='远程连接协议', default='ssh')
    protocol = serializers.ChoiceField(choices=['ssh'], label='远程连接协议', default='ssh')
    port = serializers.IntegerField(label='端口', default=22)
    comment = serializers.CharField(max_length=256, allow_blank=True, label='备注')
    # nodes = NodeSerializer(many=True, read_only=True)
    # nodes = serializers.PrimaryKeyRelatedField(many=True, queryset=Node.objects.all())
    # nodes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Server
        read_only_fields = []

    # @staticmethod
    # def get_provider_name(server):
    #     if server.provider:
    #         return server.provider.name
    #     return None


    def create(self, validated_data):
        # nodes_list = validated_data.pop('nodes', [])
        # # 如果没指定节点则使用默认节点
        # if not nodes_list:
        #     nodes_list = [Node.default_node('SERVERS')]
        nodes_list = [Node.default_node('SERVERS')]
        instance = Server.objects.create(**validated_data)
        instance.nodes.add(*nodes_list)
        return instance


    def update(self, instance, validated_data):
        # nodes_list = validated_data.pop('nodes', [])
        Server.objects.filter(id=instance.id).update(**validated_data)
        # DEFAULT node
        # if not nodes_list:
        #     nodes_list = [Node.default_node('SERVERS')]
        #
        # instance.nodes.set(nodes_list)
        return instance


class SaltServerSerializer(serializers.Serializer):
    '''
    通过salt添加服务器
    '''
    id = serializers.UUIDField()
    provider = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all(),
                                                  many=False, label='供应商',
                                                  allow_null=True, allow_empty=True)
    provider_name = serializers.SerializerMethodField()
    saltID = serializers.CharField(max_length=128, label='服务器ID')
    env = serializers.ChoiceField(choices=Server.ENV, label='环境')
    planform = serializers.CharField(max_length=56, label='平台')
    os = serializers.CharField(max_length=128, label='操作系统')
    cpu_model = serializers.CharField(max_length=256, label='CPU类型')
    cpu_arch = serializers.CharField(max_length=32, label='CPU类型')
    cpu_count = serializers.IntegerField(label='CPU类型', allow_null=True)
    # memory = serializers.CharField(max_length=32, label='内存')
    hostname = serializers.CharField(max_length=128, label='主机名')
    _IP = serializers.IPAddressField(allow_null=True, allow_blank=True, label='连接IP')
    innerIps = serializers.ListField(allow_empty=True, allow_null=True, write_only=True)
    publicIps = serializers.ListField(allow_empty=True, allow_null=True, write_only=True)
    ram = serializers.DictField(allow_null=True, write_only=True)
    comment = serializers.CharField(max_length=256, required=False, allow_blank=True, allow_null=True, label='备注')
    created = serializers.DateTimeField(read_only=True)
    nodes = NodeSerializer(many=True, read_only=True)

    class Meta:
        model = Server
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Server.objects.all(),
                fields=('saltID',),
                message=("saltID 必须唯一")
            )
        ]
    @staticmethod
    def get_provider_name(server):
        try:
            if server.provider:
                return server.provider.name
        except Exception:
            return None

    def getInstance(self, saltID):
        try:
            return Server.objects.get(saltID__exact=saltID)
        except Server.DoesNotExist:
            return None
        except Exception as e:
            raise serializers.ValidationError("服务器错误")

    def create(self, validated_data):
        # instance = self.getInstance(validated_data.get('saltID', None))
        # if instance:
        #     return self.update(instance, validated_data)
        nodes_list = [Node.default_node('SERVERS')]
        instance = Server.objects.create(**init_kwargs(Server, **validated_data))
        instance.nodes.add(*nodes_list)
        self.__check_all(instance, validated_data)
        return instance

    def check_inner_ip(self, instance, innerIps):
        ip_queryset = instance.innerIpAddress.all()
        current_ip_objs = []
        for ip in innerIps:
            try:
                ip_obj = ip_queryset.get(ip__exact=ip)
            except Ip.DoesNotExist:
                ip_obj = Ip.objects.create(ip=ip, inner=instance)
            current_ip_objs.append(ip_obj)
        self.cleanip(ip_queryset, current_ip_objs)

    def check_public_ip(self, instance, publicIps):
        ip_queryset = instance.publicIpAddress.all()
        current_ip_objs = []
        for ip in publicIps:
            try:
                ip_obj = ip_queryset.get(ip__exact=ip)
            except Ip.DoesNotExist:
                ip_obj = Ip.objects.create(ip=ip, public=instance)
            current_ip_objs.append(ip_obj)
        self.cleanip(ip_queryset, current_ip_objs)

    def check_memory(self, instance, memory):
        try:
            # 更新内存信息
            if instance.memory.memory_info != memory:
                for attr, value in memory.items():
                    setattr(instance.memory, attr, value)
                instance.memory.save()
        except Ram.DoesNotExist:
            # 创建内存信息
            Ram.objects.create(**memory, server=instance)

    def __check_all(self, instance, validated_data):
        innerIps = validated_data.get('innerIps', None)
        publicIps = validated_data.get('publicIps', None)
        memory = validated_data.get('ram', None)

        self.check_memory(instance, memory)
        self.check_inner_ip(instance, innerIps)
        self.check_public_ip(instance, publicIps)

    def update(self, instance, validated_data):
        # for attr, value in validated_data.items():
        #     setattr(instance, attr, value)
        # instance.save()
        Server.objects.filter(id=instance.id).update(**validated_data)
        self.__check_all(instance, validated_data)
        return instance

    def to_representation(self, instance):
        ret = super(SaltServerSerializer, self).to_representation(instance)

        if ret.get('cloud'):
            ret['cloud'] = {
                'id': instance.cloud.id,
                'name': instance.cloud.name
            }
        ret['Ips'] = {
            'innerIps': [ip.ip for ip in instance.innerIpAddress.all()],
            'publicIps': [ip.ip for ip in instance.publicIpAddress.all()]
        }
        ret['protocol'] = instance.protocol
        ret['port'] = instance.port

        try:
            ret['ram'] = instance.memory.memory_info
        except Exception as e:
            ret['ram'] = {}
        return ret

    def cleanip(self, ip_queryset, current_ip_objs):
        not_exists_ip = set(ip_queryset) - set(current_ip_objs)
        for obj in not_exists_ip:
            obj.delete()