from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api import user, group

router = DefaultRouter()
router.register('users', user.UserProfileViewSet, basename='users')
router.register('groups', group.UserGroupleViewSet, basename='groups')
router.register('password', user.ChangeUserPasswordViewSet, base_name="password")



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^user/(?P<pk>[a-z0-9\-]+)/groups/', user.UserUpdateGroupApi.as_view(), name='user-update-group'),
    url(r'^user/regist/', user.UserRegistAPIView.as_view(), name='user-regist'),
    # url(r'^users/(?P<pk>[a-z0-9\-]+)/password/', user.UserChangePasswordAPI.as_view(), name='change-user-password'),
]