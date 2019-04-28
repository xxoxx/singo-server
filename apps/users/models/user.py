__author__ = 'Singo'

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import json


class User(AbstractUser):
    """
    用户
    """
    ROLES = (
        ('Admin', '超级管理员'),
        ('User', '普通用户'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=32, unique=True, verbose_name='用户名')
    email = models.EmailField(max_length=128, unique=True, verbose_name='邮箱')
    name = models.CharField(max_length=128, verbose_name='姓名', null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, verbose_name='头像')
    family = models.ManyToManyField('users.UserGroup', related_name='members',
                                    blank=True, verbose_name='用户组')
    role = models.CharField(choices=ROLES, default='User', max_length=10, blank=True,
                            verbose_name='角色')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    wechat = models.CharField(max_length=30, null=True, blank=True, verbose_name='微信号')
    dingTalk = models.CharField(max_length=30, null=True, blank=True, verbose_name='钉钉号')
    comment = models.TextField(max_length=256, blank=True, verbose_name='备注')
    is_first_login = models.BooleanField(default=True)
    _properties = json.dumps({
        'activate_ldap': False
    })
    properties = models.TextField(default=_properties, verbose_name='扩展属性')

    @property
    def password_raw(self):
        raise AttributeError('Password raw is not a readable attribute')

    @password_raw.setter
    def password_raw(self, password_raw):
        return super().set_password(password_raw)

    def is_owner(self, obj):
       if self == obj:
           return True
       else:
           return False

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        db_table = 'auth_user'
        is_purview = True

class LoginLog(models.Model):
    LOGIN_TYPE = (
        ('TOKEN', 'Token Auth'),
        ('BASIC', 'Basic Auth'),
        ('JWT', 'JTW Auth'),
        ('OA', 'OA Auth'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=32, verbose_name='用户名')
    type = models.CharField(choices=LOGIN_TYPE, max_length=16, verbose_name='登录方式')
    ip = models.GenericIPAddressField(verbose_name='登录IP')
    city = models.CharField(max_length=128, blank=True, null=True, verbose_name='登录地址')
    agent = models.CharField(max_length=256, blank=True, null=True, verbose_name='游览器引擎')
    status  = models.BooleanField(max_length=1, default=True, verbose_name='状态')
    logined = models.DateTimeField(auto_now=True, verbose_name='登录时间')

    class Meta:
        verbose_name = '登录日志'
        verbose_name_plural = verbose_name


