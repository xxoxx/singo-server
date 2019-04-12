from django.db import models
import uuid

from .node import Node

class Server(models.Model):
    PLANFORM_TYPE = (
        ('Linux', 'Linux'),
        ('Windows', 'Windows'),
        ('Solaris', 'solaris'),
        ('Unknow', 'Unknow'),
    )

    PROTOCOL = (
        ('ssh', 'ssh'),
    )
    # important
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    hostname = models.CharField(max_length=128, db_index=True, verbose_name='主机名')
    saltID = models.CharField(max_length=128, db_index=True, verbose_name='服务器ID',
                              null=True, default=None, unique=True)
    # os
    planform = models.CharField(max_length=56, choices=PLANFORM_TYPE, default='Unknow', verbose_name='平台类型')
    os = models.CharField(max_length=128, verbose_name='操作系统类型')
    # cpu
    cpu_model = models.CharField(null=True, max_length=256, verbose_name='CPU类型')
    cpu_arch = models.CharField(null=True, max_length=32, verbose_name='CPU架构')
    cpu_count = models.IntegerField(null=True, verbose_name='cpu内核数')
    # memory
    # memory = models.CharField(max_length=32, verbose_name='内存')
    # connect
    protocol = models.CharField(max_length=8, choices=PROTOCOL, default='ssh', verbose_name='远程连接协议')
    port = models.IntegerField(default=22, verbose_name='远程连接端口')
    _IP = models.GenericIPAddressField(max_length=32, verbose_name='IP', blank=True, null=True)
    # others
    comment = models.TextField(max_length=256, blank=True, null=True, verbose_name='备注')
    created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='创建时间')
    provider = models.ForeignKey('Provider', blank=True, null=True)
    # node
    nodes = models.ManyToManyField('Node', related_name='server', verbose_name='节点')

