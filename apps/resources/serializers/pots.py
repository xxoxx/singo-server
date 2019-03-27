__author__ = 'singo'
__datetime__ = '2019/1/14 3:12 PM '

from rest_framework import serializers

from ..models.common import Pots

class PotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pots
        fields = '__all__'
        read_only_fields = ('id', 'resources_name')
