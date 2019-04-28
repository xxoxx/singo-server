from django.db import models
import uuid

from users.models import User
from resources.models import Server


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=64, unique=True, verbose_name='项目名')
    servers = models.ManyToManyField(Server, verbose_name='主机')
    jenkins_job = models.CharField(max_length=128, verbose_name='jenkis job')
    gitlab_project = models.CharField(max_length=128, verbose_name='gitlab project')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    creator = models.ForeignKey(User, null=False, related_name='project_creator', verbose_name='创建者')
    desc = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目配置'
        verbose_name_plural = verbose_name


class DeploymentOrder(models.Model):
    STATUS = (
        (0, '待审核'),
        (1, '待上线'),
        (2, '上线中'),
        (3, '已上线'),
        (4, '未通过'),
        (5, '上线失败')
    )

    ENV = (
        (0, '生产'),
        (1, '预发布'),
        (2, '测试')
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=128, blank=False, null=False, verbose_name='标题')
    project = models.ForeignKey(Project, blank=False, null=False, related_name='order', verbose_name='项目')
    env = models.CharField(choices=ENV, default=0, max_length=3, verbose_name='发布环境')
    branche = models.CharField(max_length=64, blank=False, null=False, verbose_name='分支')
    commit_id = models.CharField(max_length=32, blank=False, null=False, verbose_name='commit id')
    commit = models.CharField(max_length=256, blank=False, null=False, verbose_name='git commit')
    content = models.TextField(max_length=512, blank=True, null=True, verbose_name='上线描述及影响')
    applicant = models.ForeignKey(User, blank=False, null=False, related_name='dmo_applicant', verbose_name='申请人')
    reviewer = models.ForeignKey(User, blank=False, null=False, related_name='dmo_reviewer', verbose_name='审核人')
    assign_to = models.ForeignKey(User, null=False, blank=False, related_name='dmo_assigned', verbose_name='上线人')
    apply_time = models.DateTimeField(auto_now_add=True, verbose_name='申请时间')
    status = models.CharField(choices=STATUS, default=0, max_length=3, verbose_name='状态')
    # log = models.CharField(max_length=128, verbose_name='日志路径')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '上线申请'
        verbose_name_plural = verbose_name
        ordering = ['-apply_time']
