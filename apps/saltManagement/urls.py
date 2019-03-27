from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api import saltkey
from .api import saltcmd


# router = DefaultRouter()
# router.register('users', user.UserProfileViewSet, basename='users')

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^key/$', saltkey.SaltKeyAPI.as_view(), name='salt-key'),
    url(r'^cmd/script/$', saltcmd.SaltCmdScriptAPI.as_view(), name='salt-cmd-script'),
    url(r'^test/', saltkey.Test.as_view(), name='salt-test'),
    ]