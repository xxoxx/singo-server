from django.db import models
import uuid

from users.models.user import User

class WorkOrder(models.Model):
    TYPE = (
        (0, '其他'),
        (1, '项目部署'),
        (2, '计划任务'),
        (3, '数据库'),
    )

    STATUS = (
        (0, '待处理'),
        (1, '处理中'),
        (2, '已完成'),
        (3, '已失败'),
        (4, '已拒绝'),
        (5, '已关闭'),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=128, verbose_name='工单标题', blank=False, null=False)
    type = models.IntegerField(choices=TYPE, default=0, verbose_name='工单类型')
    contents = models.TextField(verbose_name='工单内容', null=False, blank=False)
    # 数据库类型的工单要求contents写的是sql,以便自动去执行sql
    comment = models.TextField(max_length=256, blank=True, null=True, verbose_name='备注')
    applicant = models.ForeignKey(User, verbose_name='申请者', related_name='wd_applicant')
    designator = models.ForeignKey(User, verbose_name='指派给')
    current_processor = models.ForeignKey(User,null=True, blank=True, verbose_name='分发给', related_name='wd_current_processor')
    finally_processor = models.ForeignKey(User, null=True, blank=True, verbose_name='最终处理者', related_name='wd_finally_processor')
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='工单状态')
    result = models.TextField(verbose_name='处理结果', blank=True, null=True)
    applied = models.DateTimeField(auto_now=True, verbose_name='申请时间')
    completed = models.DateTimeField(auto_now=True, verbose_name='处理完成时间')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '工单系统'
        verbose_name_plural = verbose_name
        ordering = ['-applied']
        is_purview = True

        # permissions = (
        #     ('workOrder_test', '测试'),
        # )