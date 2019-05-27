__author__ = 'singo'
__datetime__ = '2019/5/27 10:02 AM'


from rest_framework.decorators import api_view
from rest_framework.response import Response
from os import getenv
from django.conf import settings

@api_view(['GET'])
def devops_info(request):
    data = {
        'env': getenv('devops_env', 'dev'),
        'log_level': settings.LOG_LEVEL
    }
    return Response(data)