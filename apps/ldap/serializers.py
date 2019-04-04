__author__ = 'singo'
__datetime__ = '2019/4/3 4:25 PM '

from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(required=False, read_only=True)