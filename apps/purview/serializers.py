__author__ = 'singo'
__datetime__ = '2019/3/4 4:33 PM '

from rest_framework import serializers
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

# from users.models.user import User
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthPermissonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(AuthPermissonSerializers, self).to_representation(instance)
        ret['content_type'] = {
            'id': instance.content_type.id,
            'app': instance.content_type.app_label,
            'model': instance.content_type.model
        }
        ret['node'] = '{}.{}'.format(instance.content_type.app_label, instance.codename)
        return ret

class ContentTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(ContentTypeSerializers, self).to_representation(instance)
        app = apps.get_app_config(ret['app_label'])
        model = app.get_model(ret['model'])
        ret['name'] = model._meta.verbose_name

        return ret

class PermissionGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
        read_only_fields = ['id']


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(required=False, read_only=True)


