from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api.user_permission import UserPermissionsViewSetV2
from .api.group_permission import GroupPermissionsViewsetV2

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('user-permissions', UserPermissionsViewSetV2, base_name='user-permissions-v2')
router.register('group-permissions', GroupPermissionsViewsetV2, base_name='user-permissions-v2')



urlpatterns = [
    url(r'^', include(router.urls)),
    ]