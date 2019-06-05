__author__ = 'singo'
__datetime__ = '2019/4/25 3:30 PM '


from django.conf import settings
from gitlab import Gitlab

class GitlabAPI(object):
    def __init__(self):
        self.__gls = [Gitlab(gitlab.get('URL'), gitlab.get('TOKEN'), api_version=4) for gitlab in settings.GITLABS]

    def get_user_projects(self):
        projects = []

        for gl in self.__gls:
            projects.extend(gl.projects.list(all=True))

        return projects

    def get_project_branchs(self, path_with_namespace):
        branches = []
        for gl in self.__gls:
            try:
                projects = gl.projects.get(path_with_namespace)
                branches.append(projects.branches.list(all=True))
            except:
                pass
        return branches


gitlab_api = GitlabAPI()

