__author__ = 'singo'
__datetime__ = '2019/4/3 4:19 PM '

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ldap3 import LEVEL, SUBTREE, BASE, MODIFY_REPLACE
from devops.settings import LADPAPI
import json

from .serializers import LdapSerializer
from common.apis import ldap_conn, oaapi
from common.permissions import DevopsPermission
from common.utils import logger, id_generator


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

    @action(detail=False, methods=['post'], name='activate-ldap',
            url_path='activate-ldap', **{'perms_map': {'POST':['{}.ldap_activate']}})
    def activate_ldap(self, request, pk=None):
        user_info  = oaapi.get_userinfo(request.user.username)
        password = request.data.get('password', 'hello1234')
        attributes = {}

        if user_info:
            attributes['sn'] = user_info.get('pinyinhead')
            attributes['givenName'] = user_info.get('pinyinhead')
            attributes['displayName'] = user_info.get('name')
            attributes['uid'] = user_info.get('pinyin')
            attributes['userPassword'] = password
            attributes['mobile'] = user_info.get('telNumber')
            attributes['mail'] = user_info.get('emailAddress')
            attributes['postalAddress'] = user_info.get('address')
            attributes['objectClass'] = ['shadowAccount', 'person', 'organizationalPerson', 'inetOrgPerson']

            user_dn = 'cn={},{}'.format(attributes['uid'], LADPAPI['LDAP_BASE_DN'])
            ldap_conn.add(user_dn, attributes=attributes)

            if ldap_conn.result['result'] != 0:
                logger.critical(str(ldap_conn.result))
                raise LdapError

            # 设置数据库标记
            properties = json.loads(request.user.properties)
            properties['activate_ldap'] = True
            request.user.properties = json.dumps(properties)
            request.user.save()
        else:
            return Response({'detail':'获取OA信息失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': 'LDAP已经激活, 登录用户:{}'.format(attributes['uid'])})

    @action(detail=False, methods=['post'], name='change-password',
            url_path='change-password', **{'perms_map': {'POST':['{}.password_change']}})
    def change_password(self, request, pk=None):
        user_info = oaapi.get_userinfo(request.user.username)
        password = request.data.get('password', 'hello1234')
        if user_info:
            uid = user_info.get('pinyin')
            user_dn = 'cn={},{}'.format(uid, LADPAPI['LDAP_BASE_DN'])
            ldap_conn.modify(user_dn, {'userPassword': [(MODIFY_REPLACE, [password])]})

            if ldap_conn.result['result'] != 0:
                logger.critical(str(ldap_conn.result))
                raise LdapError
        else:
            return Response({'detail':'修改密码失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'detail':'修改密码成功'})


from rest_framework.exceptions import APIException
class LdapError(APIException):
    status_code = 400
    default_detail = 'ldap服务器返回错误'
    default_code = 'invalid'