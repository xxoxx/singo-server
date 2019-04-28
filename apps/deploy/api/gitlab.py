__author__ = 'singo'
__datetime__ = '2019/4/25 4:08 PM '

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.apis import gitlab_api
from common.utils import logger
from common.permissions import DevopsPermission


class GitlabProjectsList(APIView):
    def get(self, request, format=None):
        data = []
        try:
            projects =  gitlab_api.get_user_projects()
            for p in projects:
                data.append(
                    {
                        'id': p.id,
                        'name': p.name,
                        'description': p.description,
                        'path_with_namespace': p.path_with_namespace
                    }
                )
        except Exception as e:
            logger.error(e)
            return Response({'detail': '获取gitlab项目失败'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data)

class GitlabProjectBranchesList(APIView):
    def get(self, request, format=None):
        data = []
        path_with_namespace = request.GET.get('path_with_namespace')
        try:
            branches = gitlab_api.get_project_branchs(path_with_namespace)

            if len(branches) > 1:
                return Response({'detail': '多个gitlab中存在多个相同的工程'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            elif len(branches) == 1:
                data = [{
                            'name': branch.name,
                            'commit_id': branch.commit.get('short_id'),
                            'message': branch.commit.get('message'),
                            'created': branch.commit.get('created_at')
                        }for branch in branches[0]]
        except Exception as e:
            logger.error(e)
            return Response({'detail': '获取项目分支失败'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data)