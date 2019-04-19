from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api import server, provider, node

router = DefaultRouter()
router.register('server', server.ServerViewSet, basename='server')
router.register('salt-server', server.SaltServerViewSet, basename='salt-server')
router.register('provider', provider.ProviderViewSet, basename='provider')
router.register('node/root', node.NodeRootViewSet, basename='node-root')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^node/(?P<pk>[a-z0-9\-]+)/$', node.NodeChildAPIView.as_view(), name='node-child'),
    url(r'^node/(?P<pk>[a-z0-9\-]+)/children/$', node.NodeChildrenAPIView.as_view(), name='node-children'),
    url(r'^node/(?P<pk>[a-z0-9\-]+)/assets/$', node.NodeAssetsApi.as_view(), name='node-assets'),
]