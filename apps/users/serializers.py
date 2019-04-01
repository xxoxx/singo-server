from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password

from .models import User, UserGroup

class UserSerializer(serializers.ModelSerializer):
    # groups = serializers.PrimaryKeyRelatedField(many=True, queryset=UserGroup.objects.all())
    family_names = serializers.SerializerMethodField()
    class Meta:
        model = User
        exclude = ('password', 'user_permissions',
                   'first_name', 'last_name', 'groups')
        read_only_fields=['id', 'date_joined', 'is_first_login']

    @staticmethod
    def get_family_names(user):
        return [family.name for family in user.family.all()]


    # def create(self, validated_data):
    #     from common.utils import id_generator as password_generator
    #     from .utils import send_user_created_mail
    #     password = password_generator()
    #     validated_data['password'] = make_password(password)
    #     user = super(UserSerializer, self).create(validated_data)
    #     user.password = password
    #     # 用户创建成功发送邮件
    #     send_user_created_mail(user)
    #     return user

    # def validate_username(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return value

class UserGroupSerializer(serializers.ModelSerializer):
    # creator = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), many=False)
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    members_names = serializers.SerializerMethodField()
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserGroup
        fields = '__all__'
        read_only_fields = ['id', 'created', 'creator']

    @staticmethod
    def get_members_names(group):
        return [member.name for member in group.members.all()]

    def to_representation(self, instance):
        ret =  super(UserGroupSerializer, self).to_representation(instance)
        ret['creator'] = {'id':instance.creator.id, 'name': instance.creator.name}
        return ret

    def update(self, instance, validated_data):
        validated_data.pop('creator')
        return super(UserGroupSerializer, self).update(instance, validated_data)

class UserUpdateGroupSerializer(serializers.ModelSerializer):
    family = serializers.PrimaryKeyRelatedField(many=True, queryset=UserGroup.objects.all())
    class Meta:
        model = User
        fields = ['id', 'family']

class ChangeUserPasswordSerializer(serializers.ModelSerializer):
    '''
    修改用户密码
    '''
    originalPassword = serializers.CharField(allow_blank=True,
                                             style={'input_type': 'password'},
                                             label='原密码')
    password = serializers.CharField(style={'input_type': 'password'},
                                             label='密码')
    class Meta:
        model = User
        fields = ['originalPassword', 'password']

    def validate(self, data):
        owner = self.context['request'].user
        # 当用户为普通用户的时候只能修改本人密码且需要原密码验证
        # 非管理员用户修改其他用户会返回错误
        if not owner.is_staff:
            if not check_password(data['originalPassword'], owner.password):
                raise PasswordError()
        data['password'] = make_password(data['password'])

        return data


    def to_representation(self, instance):
        return {'detail': '密码修改成功'}

class UserRegistSerializer(serializers.ModelSerializer):
    password= serializers.CharField(style={'input_type': 'password'}, label='密码')
    class Meta:
        model = User
        fields = ['username', 'name', 'password', 'email', 'phone']

    def create(self, validated_data):
        from common.utils import id_generator as password_generator
        from .utils import send_user_created_mail
        password = password_generator()
        validated_data['password'] = make_password(password)
        user = super(UserRegistSerializer, self).create(validated_data)
        user.password = password
        # 用户创建成功发送邮件
        send_user_created_mail(user)
        return user

from rest_framework.exceptions import APIException
class PasswordError(APIException):
    status_code = 400
    default_detail = '原密码错误'
    default_code = 'invalid'