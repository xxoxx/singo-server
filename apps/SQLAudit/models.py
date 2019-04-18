from django.db import models

class Permission(models.Model):
    '''
    对于没有model的apps需要添加默认表来添加权限
    '''
    name = models.CharField(max_length=128, verbose_name='名称')

    class Meta:
        verbose_name = '权限控制'
        verbose_name_plural = verbose_name
        is_purview = True