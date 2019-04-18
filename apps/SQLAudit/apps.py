from django.apps import AppConfig


class SqlauditConfig(AppConfig):
    name = 'SQLAudit'
    verbose_name = 'SQL审核展示'
    is_purview = True
