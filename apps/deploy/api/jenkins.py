__author__ = 'singo'
__datetime__ = '2019/4/26 10:07 AM '

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.apis import jenkins_api
from common.utils import logger
from common.permissions import DevopsPermission


class JenkinsJobList(APIView):
    def get(self, request, format=None):
        data = []
        try:
            jobs = jenkins_api.get_all_jobs()
            data = [{
                    'name': job['name'],
                    'url': job['url']
                    }for job in jobs]

        except Exception as e:
            logger.error(e)
            return Response({'detail': '获取jenkins job 列表失败'})

        return Response(data)

