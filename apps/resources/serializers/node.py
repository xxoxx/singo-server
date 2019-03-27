__author__ = 'singo'
__datetime__ = '2019/1/10 1:55 PM '

from rest_framework import serializers

from ..models.node import Node

class NodeSerializer(serializers.ModelSerializer):
    # 可以是自动赋值的
    # key = serializers.CharField(max_length=64, allow_null=True, allow_blank=True)
    class Meta:
        model = Node
        fields = '__all__'
        read_only_fields = ('id', 'key', 'child_mark')

class NodeChildrenSerializer(serializers.ModelSerializer):
    # 可以是自动赋值的
    key = serializers.CharField(max_length=64, allow_null=True, allow_blank=True)
    name = serializers.CharField(max_length=32, allow_blank=False, allow_null=False)
    class Meta:
        model = Node
        fields = '__all__'
        read_only_fields = ('id',)

class NodeAssetsSerializer(serializers.Serializer):
    related_name = serializers.CharField(max_length=32, allow_blank=False, allow_null=False)
    resource_id = serializers.ListField(allow_empty=False, allow_null=False)