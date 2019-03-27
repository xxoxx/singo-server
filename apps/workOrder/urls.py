from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .api import WorkOrderViewset, Test

router = DefaultRouter()
router.register('workorder', WorkOrderViewset, basename='workOrder')
router.register('test', Test, basename='test')



urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^test/', Test.as_view(), name='salt-test'),
    # url(r'^user/(?P<pk>[a-z0-9\-]+)/groups/', user.UserUpdateGroupApi.as_view(), name='user-update-group'),
]