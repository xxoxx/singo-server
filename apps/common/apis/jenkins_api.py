__author__ = 'singo'
__datetime__ = '2019/4/26 9:25 AM '


from django.conf import settings
from jenkins import Jenkins, JenkinsException
import requests
import os

from common.utils import logger


class JenkinsAPI(object):
    def __init__(self):
        self.__server = Jenkins(settings.JENKINS.get('URI'))

    def get_all_jobs(self):
        return self.__server.get_all_jobs()

    def get_next_build_number(self, name):
        return self.__server.get_job_info(name)['nextBuildNumber']

    def build_job(self, name, parameters=None):
        return self.__server.build_job(name=name, parameters=parameters)

    def get_build_info(self, name, build_number):
        try:
            return self.__server.get_build_info(name, build_number)
        except Exception as e:
            logger.exception(e)
            return None

    def get_build_console_output(self, name, number):
        try:
            return self.__server.get_build_console_output(name, number)
        except JenkinsException as e:
            logger.exception(e)
            return None

    def download_package(self, package_url, name, build_number):
        URI = settings.JENKINS.get('URI')
        download_url = '{}/job/{}/{}/artifact/{}'.format(URI, name, build_number, package_url)
        local_filename = download_url.split('/')[-1]
        code_path = os.path.join(settings.DEPLOY.get('CODE_PATH'), 'packages')
        local_full_filename = os.path.join(code_path, local_filename)

        # with requests.get(url, stream=True,
        # auth=HTTPBasicAuth("zhoujinliang", "117c911a35acf51e428e29f3ccb363f53f")) as r:
        with requests.get(download_url, stream=True) as r:
            r.raise_for_status()
            with open(local_full_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
        return local_full_filename

    def cancel_build(self, name, queue_id, build_number):
        try:
            self.__server.cancel_queue(queue_id)
            self.__server.stop_build(name, build_number)
        except Exception as e:
            logger.error(e)

    def test(self):
        return self.__server.cancel_queue(3590)
        # # return self.__server.stop_build('devops', 98)
        return self.__server.get_queue_info()

jenkins_api = JenkinsAPI()
