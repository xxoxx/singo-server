__author__ = 'Singo'

import uuid
from django.db import models


class UserGroup(models.Model):
    """
    用户组
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=30, unique=True, verbose_name='用户组名称')
    comment = models.TextField(max_length=256, blank=True, verbose_name='备注')
    # created = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    creator = models.ForeignKey("User", null=False, related_name='creator', verbose_name='创建者')

    class Meta:
        ordering = ['name']
        verbose_name = '用户组'
        verbose_name_plural = verbose_name
        is_purview = True


    def __str__(self):
        return self.name
