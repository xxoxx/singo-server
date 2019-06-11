from django.db import models
import uuid
from django.core.exceptions import ValidationError

from users.models import User
from resources.models import Server
from .common import *

STATUS = (
    (D_UNREVIEWED, '待审核'),
    (D_PENDING, '待执行'),
    (D_RUNNING, '运行中'),
    (D_SUCCESSFUL, '成功'),
    (D_REJECTED, '拒绝'),
    (D_FAILED, '失败')
)

ENV = (
    (PRO, '生产环境'),
    (PRE, '预发布环境'),
    (TEST, '测试环境')
)

TYPE = (
    (ONLINE, '上线'),
    (ROLLBACK, '回滚'),
    (REONLONE, '重新上线')
)

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=64, unique=True, verbose_name='项目名')
    # servers = models.ManyToManyField(Server, blank=True, verbose_name='主机')
    servers = models.ManyToManyField(Server, blank=True, verbose_name='主机')
    jenkins_job = models.CharField(max_length=128, verbose_name='jenkis job')
    gitlab_project = models.CharField(max_length=128, verbose_name='gitlab project')
    package_url = models.CharField(max_length=128, null=False, blank=False, verbose_name='jenkins 打包路径')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    creator = models.ForeignKey(User, null=False, related_name='project_creator', verbose_name='创建者')
    desc = models.TextField(max_length=256, blank=True, null=True, verbose_name='描述')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目配置'
        verbose_name_plural = verbose_name

class DeploymentOrder(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=128, blank=False, null=False, verbose_name='标题')
    project = models.ForeignKey(Project, blank=False, null=False, related_name='order',
                                verbose_name='项目',  on_delete=models.PROTECT)
    type = models.IntegerField(choices=TYPE, default=ONLINE, verbose_name='类型')
    env = models.IntegerField(choices=ENV, default=PRO, verbose_name='部署环境')
    # parent_env =
    branche = models.CharField(max_length=64, blank=False, null=False, verbose_name='分支')
    commit_id = models.CharField(max_length=64, blank=False, null=False, verbose_name='commit id')
    commit = models.CharField(max_length=256, blank=False, null=False, verbose_name='git commit')
    content = models.TextField(max_length=512, blank=True, null=True, verbose_name='上线描述及影响')
    applicant = models.ForeignKey(User, blank=False, null=False, related_name='dmo_applicant',
                                  verbose_name='申请人',  on_delete=models.PROTECT)
    reviewer = models.ForeignKey(User, blank=False, null=False, related_name='dmo_reviewer',
                                 verbose_name='审核人',  on_delete=models.PROTECT)
    assign_to = models.ForeignKey(User, null=False, blank=False, related_name='dmo_assigned',
                                  verbose_name='上线人',  on_delete=models.PROTECT)
    apply_time = models.DateTimeField(auto_now_add=True, verbose_name='申请时间')
    complete_time = models.DateTimeField(null=True, verbose_name='结束时间')
    status = models.IntegerField(choices=STATUS, default=D_UNREVIEWED, verbose_name='状态')
    result_msg = models.TextField(blank=True, verbose_name='结果')
    deploy_times = models.IntegerField(default=0, verbose_name='部署次数')

    def __str__(self):
        return self.title


    # 根据环境获取需要部署的服务器
    @property
    def deploy_servers(self):
        return [s.saltID for s in self.project.servers.all() if s.env == self.env]

    @property
    def servers_ip(self):
        return ','.join(s._IP for s in self.deploy_servers)

    @property
    def servers_saltID(self):
        return ','.join(s.saltID for s in self.deploy_servers)

    class Meta:
        verbose_name = '上线申请'
        verbose_name_plural = verbose_name
        ordering = ['-apply_time']

HISTORY_STATUS = (
    (H_UNKNOWN, '未知'),
    (H_CANCELED, '取消'),
    (H_SUCCESSFUL, '成功'),
    (H_FAILED, '失败')
)

class History(models.Model):
    order_id = models.UUIDField(verbose_name='上线单ID')
    deploy_times = models.IntegerField(verbose_name='关联工单部署次数')
    title = models.CharField(max_length=128, verbose_name='标题')
    project_name = models.CharField(max_length=64, verbose_name='项目名')
    env = models.IntegerField(choices=ENV, default=PRO, verbose_name='部署环境')
    type = models.IntegerField(choices=TYPE, default=ONLINE, verbose_name='类型')
    servers_ip = models.TextField(verbose_name='部署服务器IP')
    servers_saltID = models.TextField(verbose_name='部署服务器saltID')
    branche = models.CharField(max_length=64, verbose_name='分支')
    commit_id = models.CharField(max_length=64, verbose_name='commit id')
    commit = models.CharField(max_length=256, verbose_name='git commit')
    jk_number = models.IntegerField(verbose_name='jenkins 构建ID')
    jk_result = models.CharField(max_length=32,default='unknown', verbose_name='jenkins 构建结果')
    applicant = models.CharField(max_length=32, verbose_name='申请人')
    reviewer = models.CharField(max_length=32, verbose_name='审核人')
    assign_to = models.CharField(max_length=32, verbose_name='上线人')
    result = models.IntegerField(choices=HISTORY_STATUS, default=H_UNKNOWN, verbose_name='状态')
    start = models.DateTimeField(auto_now_add=True, verbose_name='开始时间')
    end = models.DateTimeField(null=True, verbose_name='结束时间')
    log_file = models.CharField(max_length=128, verbose_name='部署日志')
    error_msg = models.TextField(null=True, verbose_name='异常信息')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '历史记录'
        verbose_name_plural = verbose_name
        ordering = ['-id']
        unique_together = ('order_id', 'deploy_times')


def validate_parent(parent):
    if parent and parent.parent:
        raise ValidationError(
            '%(value)s 不是顶级, 只允许关联到顶级',
            params={'value': parent.name},
        )

class DeployEnv(models.Model):
    name = models.CharField(max_length=56, verbose_name='名称', unique=True)
    code = models.CharField(max_length=56, verbose_name='code')
    parent = models.ForeignKey('DeployEnv', null=True, validators=[validate_parent])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '部署环境'
        verbose_name_plural = verbose_name

def validate_sub(parent):
    if parent and not parent.parent:
        raise ValidationError(
            '%(value)s 是顶级, 只允许关联到子级',
            params={'value': parent.name},
        )

class DeployItem(models.Model):
    name = models.CharField(max_length=56, verbose_name='名称', unique=True)
    parent_env = models.ForeignKey('DeployEnv', null=False, related_name='deploy_item_parent_env',
                                   on_delete=models.PROTECT, validators=[validate_parent])
    sub_env = models.ForeignKey('DeployEnv', null=True, related_name='deploy_item_sub_env',
                                on_delete=models.PROTECT, validators=[validate_sub])
    servers = models.ManyToManyField(Server, blank=True, verbose_name='主机')