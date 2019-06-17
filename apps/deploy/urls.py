from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .api import gitlab, jenkins, project, deploy, history, order, deploy_env, env_servers_map



router = DefaultRouter()

router.register('projects', project.ProjectViewSet, base_name='projects')
router.register('deployment-orders', order.DeploymentOrderViewSet, base_name='orders')
router.register('history', history.HistoryViewSet, base_name='history')
router.register('deploy-env', deploy_env.DeployEnvViewSet, base_name='deploy-env')
router.register('env-servers', env_servers_map.EnvServersMapViewSet, base_name='env-servers')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^gitlab/projects/$', gitlab.GitlabProjectsList.as_view(), name='gitlab-projects'),
    url(r'^gitlab/branches/$', gitlab.GitlabProjectBranchesList.as_view(), name='gitlab-branches'),
    url(r'^jenkins/jobs/$', jenkins.JenkinsJobList.as_view(), name='jenkins-jobs'),
    url(r'^deploy/(?P<pk>[a-z0-9\-]+)/$', deploy.DeployAPIView.as_view(), name='deploy'),
    url(r'^redeploy/(?P<pk>[a-z0-9\-]+)/$', deploy.RedeployAPIView.as_view(), name='redeploy'),
    url(r'^deploy/(?P<pk>[a-z0-9\-]+)/log/$', deploy.DeployRealtimeLog.as_view(), name='realtime-log'),
    url(r'^deploy/(?P<pk>[a-z0-9\-]+)/webhook/$', deploy.SaltStateSLSWebhook.as_view(), name='salt-webhook'),
    url(r'^rollback/(?P<project_name>[a-z0-9\-]+)/$', order.RollBackList.as_view(), name='rollback'),
    url(r'^test/', deploy.Test.as_view(), name='test'),
    ]