from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api import LdapViewset


router = DefaultRouter()

router.register('ldap', LdapViewset, base_name='ldap')

urlpatterns = [
    url(r'^', include(router.urls)),
    ]