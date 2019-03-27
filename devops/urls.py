"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework import permissions
from drf_yasg.views import get_schema_view as yasg_get_schema_view
from drf_yasg import openapi
from django.views.static import serve
from rest_framework.routers import DefaultRouter

from rest_framework_jwt.views import obtain_jwt_token

from users.api.login import ObtainAuthTokenAndLogging, obtainJwtTokenAndLogging
from .settings import MEDIA_ROOT
from users.urls import router  as user_router
from resources.urls import router  as resources_router
schema_view = get_schema_view(title="Devops API",
                              renderer_classes=[SwaggerUIRenderer, OpenAPIRenderer])

yasg_schema_view = yasg_get_schema_view(
   openapi.Info(
      title="Devops API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

router = DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(resources_router.registry)

api_patterns = [
    url(r'^resources/v1/', include('resources.urls', namespace='api-resources', app_name='resources')),
    url(r'^users/v1/', include('users.urls', namespace='api-users', app_name='users')),
    url(r'^salt/v1/', include('saltManagement.urls', namespace='api-salt', app_name='saltManagement')),
    url(r'^workorder/v1/', include('workOrder.urls', namespace='api-work-order', app_name='workOrder')),
    url(r'^permissions/v1/', include('purview.urls', namespace='api-permissions', app_name='purview')),
]

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 文档登录的时候要用到
    url('^accounts/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^api-token-auth/', ObtainAuthTokenAndLogging.as_view()),
    # url(r'^api-jwt-token-auth/', obtain_jwt_token),
    url(r'^api-jwt-token-auth/', obtainJwtTokenAndLogging.as_view()),
    # url(r'^api/v1/', include(router.urls)),
    url(r'^api/', include(api_patterns)),
    # url(r'^resources/v1/', include('resources.urls', namespace='api-resources', app_name='resources')),
    # drf 自带文档
    url(r'^docs/', include_docs_urls('接口文档')),
    # swagger 文档
    url(r'^schema-docs/', schema_view),
    # drf_yasg 文档
    url(r'^swagger(?P<format>\.json|\.yaml)$', yasg_schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', yasg_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # redoc 不好用,但能生成json格式的文档树
    # url(r'^redoc/$', yasg_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

