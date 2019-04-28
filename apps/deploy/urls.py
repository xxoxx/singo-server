from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api import NodesAPI, DocumentsAPI


# router = DefaultRouter()
#
# router.register('ldap', LdapViewset, base_name='ldap')

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^nodes/', NodesAPI.as_view(), name='nodes'),
    url(r'^documents/', DocumentsAPI.as_view(), name='documents'),
    ]