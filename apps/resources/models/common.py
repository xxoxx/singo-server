from django.db import models
from django.core.exceptions import ValidationError

class Provider(models.Model):
    name = models.CharField(max_length=50, verbose_name='设备提供者名称', unique=True)
    code = models.CharField(max_length=50, verbose_name='设备提供者编码', unique=True)

    def __str__(self):
        return self.name

class Ip(models.Model):
    ip = models.GenericIPAddressField(db_index=True)
    inner = models.ForeignKey('Server', related_name='innerIpAddress',
                              null=True, verbose_name='内网IP地址')
    public = models.ForeignKey('Server', related_name='publicIpAddress',
                               null=True,verbose_name='外网IP地址')

    def clean(self):
        if not self.inner and not self.public:
            raise ValidationError('inner public 必须有一个为空')
        super().clean()

class Ram(models.Model):
    physical = models.IntegerField(null=True, blank=True, verbose_name='物理内存大小')
    swap = models.IntegerField(null=True, blank=True, verbose_name='交换区大小')
    server = models.OneToOneField('Server', on_delete=models.CASCADE, related_name='memory')

    @property
    def memory_info(self):
        return {'physical': self.physical, 'swap': self.swap}

class Pots(models.Model):
    '''
    资源与节点之间相互绑定, 确保每个资源只有唯一的节点
    '''
    resources_name = models.CharField(max_length=64, verbose_name='应用名称',
                                      unique=True, null=False, blank=False)
    node_name = models.CharField(max_length=32, verbose_name='节点名称',
                                 unique=True, null=False, blank=False)



