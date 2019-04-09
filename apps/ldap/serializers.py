__author__ = 'singo'
__datetime__ = '2019/4/3 4:25 PM '

from rest_framework import serializers

class LdapSerializer(serializers.Serializer):
    sn = serializers.CharField()
    givenName = serializers.CharField()
    displayName = serializers.CharField()
    uid = serializers.CharField()
    userPassword = serializers.CharField()
    mobile = serializers.CharField(max_length=11, min_length=11)
    mail = serializers.EmailField()
    postalAddress = serializers.CharField()

