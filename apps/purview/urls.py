from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api.user_permission import UserPermissionsViewSet
from .api.group_permission import GroupPermissionsViewset
from .api.permission_query import PermissonQueryViewSet, AuthPermissonViewSet
from .api.group import GroupViewSet, GroupUsersViewset, UserGroupsViewset

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('permission-query', PermissonQueryViewSet, base_name='permission-query')
router.register('auth-permissons', AuthPermissonViewSet, base_name='auth-permissons')
router.register('group', GroupViewSet, base_name='group')
# 权限组成员管理
router.register('group-users', GroupUsersViewset, base_name='group-users')
# 成员,权限组管理
router.register('user-groups', UserGroupsViewset, base_name='user-groups')
router.register('group-permissions', GroupPermissionsViewset, base_name='group-permissions')
router.register('user-permissions', UserPermissionsViewSet, base_name='user-permissions')




urlpatterns = [
    url(r'^', include(router.urls)),
    ]