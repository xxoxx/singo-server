__author__ = 'singo'
__datetime__ = '2019/2/14 10:57 AM'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import logging

from common import saltapi

logger = logging.getLogger('devops')

class SaltCmdScriptAPI(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self):
        return Response({'status': 'OK'})