__author__ = 'singo'
__datetime__ = '2019/4/3 4:19 PM '

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from ldap3 import LEVEL, SUBTREE, BASE
from devops.settings import LADPAPI
import json

from .serializers import TestSerializer
from common.apis import ldap_conn


class LdapViewset(viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = TestSerializer
    queryset = []
    # lookup_field = 'pk'
    # lookup_value_regex = '[0-9]+'

    def func(self, entries, level=1):
        item = []
        for entry in entries:
            entry_dict = json.loads(entry.entry_to_json())
            label = entry_dict.get('dn')
            child = {'label': label, 'children': []}
            ldap_conn.search(search_base=label,
                             search_filter='(objectClass=top)',
                             search_scope=LEVEL
                             )
            if level <=3:
                child['children'] = self.func(ldap_conn.entries, level+1)
            item.append(child)
        return item






    def list(self, request, *args, **kwargs):

        ldap_conn.search(search_base='dc=ztyc,dc=net',
                             search_filter='(objectClass=top)',
                             search_scope=BASE)

        data = self.func(ldap_conn.entries, level=1)

        # entries = ldap_conn.entries
        # for entry in ldap_conn.entries:
        #     entry_dict = json.loads(entry.entry_to_json())
        #     label = entry_dict.get('dn')
        #     item = {'label': label, 'children': []}
        #     ldap_conn.search(search_base=label,
        #                 search_filter='(objectClass=top)',
        #                 search_scope=LEVEL
        #                 )
        #     # entries = ldap_conn.entries
        #     for entry in ldap_conn.entries:
        #         entry_dict = json.loads(entry.entry_to_json())
        #         label = entry_dict.get('dn')
        #         sub_item = {'label':label, 'children': []}
        #
        #         ldap_conn.search(search_base=label,
        #                          search_filter='(objectClass=top)',
        #                          search_scope=LEVEL
        #                          )
        #         for entry in ldap_conn.entries:
        #             entry_dict = json.loads(entry.entry_to_json())
        #             label = entry_dict.get('dn')
        #             sub_item['children'].append({'label':label, 'children': []})
        #
        #         item['children'].append(sub_item)
        #
        #     data.append(item)


        return Response(data)

