__author__ = 'singo'
__datetime__ = '2019/4/3 4:06 PM '

from ldap3 import Connection, Server, ALL, SUBTREE, MODIFY_REPLACE, SUBTREE, LEVEL, BASE
from django.conf import settings

from common.utils import logger


try:
    _server = Server(host=settings.LADPAPI.get('LDAP_HOST'),
                    use_ssl=settings.LADPAPI.get('LDAP_USE_SSL'),
                    connect_timeout=30)

    ldap_conn = Connection(_server,
                    user=settings.LADPAPI.get('LDAP_BIND_USER_DN'),
                    password=settings.LADPAPI.get('LDAP_BIND_USER_PASSWORD'),
                    auto_bind=True, lazy=True)

    # ldap_conn.search(search_base='dc=ztyc,dc=net',
    #             search_filter='(objectClass=top)',
    #             search_scope=LEVEL
    #             )
except Exception as e:
    logger.error(e)




