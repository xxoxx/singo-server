__author__ = 'singo'
__datetime__ = '2019/4/3 4:19 PM '

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response
from ldap3 import LEVEL, SUBTREE, BASE, MODIFY_REPLACE
from devops.settings import LADPAPI
import json

from .serializers import LdapSerializer
from common.apis import ldap_conn
from common.permissions import DevopsPermission
from common.utils import logger


class LdapViewset(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    '''
    ldap people操作

    get:
        获取成员树

    get(detail):
        获取成员详情

    post:
        添加成员

    put:
        更新成员信息

    delete:
        删除成员

    '''

    permission_classes = (permissions.IsAuthenticated, DevopsPermission)
    serializer_class = LdapSerializer
    queryset = []

    perms_map = {
        'GET': ['{}.ldap_list'],
        'POST': ['{}.member_add'],
        'PUT': ['{}.member_edit'],
        'PATCH': ['{}.member_edit'],
        'DELETE': ['{}.member_delete']
    }

    def __entries_list(self, entries, level=1):
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
                child['children'] = self.__entries_list(ldap_conn.entries, level+1)
            item.append(child)
        return item

    def list(self, request, *args, **kwargs):

        ldap_conn.search(search_base='dc=ztyc,dc=net',
                             search_filter='(objectClass=top)',
                             search_scope=BASE)

        data = self.__entries_list(ldap_conn.entries, level=1)

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

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        uid = filter_kwargs.get('pk')
        search_filter = '(uid={})'.format(uid)

        ldap_conn.search(search_base=LADPAPI['LDAP_BASE_DN'],
                         search_filter=search_filter,
                         attributes=['sn', 'givenName', 'displayName', 'uid',
                                     'userPassword', 'mobile', 'mail', 'postalAddress']
                         )

        if ldap_conn.result['result'] != 0 or not ldap_conn.entries:
            logger.critical(str(ldap_conn.result))
            raise LdapError

        attributes = json.loads(ldap_conn.entries[0].entry_to_json())['attributes']
        data = {}

        for key, val in attributes.items():
            data[key] = val[0]

        return data


    def perform_create(self, serializer):
        attributes = dict(serializer.data)
        attributes['objectClass'] = ['shadowAccount', 'person', 'organizationalPerson', 'inetOrgPerson']
        user_dn = 'cn={},{}'.format(attributes['uid'], LADPAPI['LDAP_BASE_DN'])
        ldap_conn.add(user_dn, attributes=attributes)

        if ldap_conn.result['result'] != 0:
            logger.critical(str(ldap_conn.result))
            raise LdapError

    def update(self, request, *args, **kwargs):
        # 因为get_object返回的不是model对象,需要手动获取serializer
        attributes = request.data.copy()
        serializer = self.get_serializer(data=attributes)
        user_dn = 'cn={},{}'.format(attributes['uid'], LADPAPI['LDAP_BASE_DN'])
        serializer.is_valid(raise_exception=True)

        for key, val in attributes.items():
            attributes[key] = [(MODIFY_REPLACE, [val])]

        ldap_conn.modify(user_dn, attributes)

        if ldap_conn.result['result'] != 0:
            logger.critical(str(ldap_conn.result))
            raise LdapError
        return Response(data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        uid = kwargs.get('pk')
        user_dn = 'cn={},{}'.format(uid, LADPAPI['LDAP_BASE_DN'])
        ldap_conn.delete(user_dn)

        if ldap_conn.result['result'] != 0:
            logger.critical(str(ldap_conn.result))
            raise LdapError

        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.exceptions import APIException
class LdapError(APIException):
    status_code = 400
    default_detail = 'ldap服务器返回错误'
    default_code = 'invalid'