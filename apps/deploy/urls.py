from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .api import gitlab, jenkins, project, deploy



router = DefaultRouter()

router.register('projects', project.ProjectViewSet, base_name='projects')
router.register('deployment-orders', deploy.DeploymentOrderViewSet, base_name='orders')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^gitlab/projects/', gitlab.GitlabProjectsList.as_view(), name='gitlab-projects'),
    url(r'^gitlab/branches/', gitlab.GitlabProjectBranchesList.as_view(), name='gitlab-branches'),
    url(r'^jenkins/jobs/', jenkins.JenkinsJobList.as_view(), name='jenkins-jobs'),
    ]