__author__ = 'singo'
__datetime__ = '2019/1/10 1:57 PM '

from rest_framework import serializers

from ..models.common import Provider

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = "__all__"
        read_only_fields = ('id',)