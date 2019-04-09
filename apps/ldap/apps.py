from django.apps import AppConfig


class LdapConfig(AppConfig):
    name = 'ldap'
    verbose_name = 'ldap管理'
    is_purview = True
