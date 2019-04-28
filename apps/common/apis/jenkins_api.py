__author__ = 'singo'
__datetime__ = '2019/4/26 9:25 AM '


from django.conf import settings
from jenkins import Jenkins


class JenkinsAPI(object):
    def __init__(self):
        self.__server = Jenkins(settings.JENKINS.get('URI'))

    def get_all_jobs(self):
        return self.__server.get_all_jobs()


jenkins_api = JenkinsAPI()
