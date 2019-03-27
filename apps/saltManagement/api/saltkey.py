from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import logging

from common import saltapi
from common.utils import Bcolor

logger = logging.getLogger('devops')

class SaltKeyAPI(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        data = saltapi.key_list()
        return Response(data)

    def __key_operations(self, key, request):
        f = {
            'accept': saltapi.accept_key,
            'delete': saltapi.delete_key,
            'reject': saltapi.reject_key
        }.get(key, None)

        if f:
            try:
                key_id = request.data['keyID']
                data = f(key_id=key_id)
            except KeyError:
                logger.warning('找不到keyID')
                data = {'code': -1, 'detail': '参数错误'}
        else:
            data = {'code': -1, 'detail': '未找到执行函数'}
        return data

    def put(self, request, *args, **kwargs):
        data = self.__key_operations('accept', request)
        return Response(data)

    def patch(self, request, *args, **kwargs):
        data = self.__key_operations('reject', request)
        return Response(data)

    def delete(self, request, *args, **kwargs):
        data = self.__key_operations('delete', request)
        return Response(data)

class Test(APIView):
    def get(self, request, format=None):
    #     data = saltapi.get_grains_items('minion-1')
    #
    #     if data['code'] == 200:
    #         from resources.createSources.server import saveServer
    #         data = saveServer(data)

        # print(data)
        # from resources.models import Server
        # from resources.serializers import SaltServerSerializer
        # server = Server.objects.get(pk='9d20bd5985b447d083bb6d9fac6cbba3')
        # serializer = SaltServerSerializer(server, data={'os': 'ubuntu','publicIps':['114.114.114.114']}, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        # else:
        #     print(serializer.errors)
        # print(server.innerIpAddress.all())

        # from resources.models.server import Server
        # s = Server.objects.create(**{'hostname': 'test14','provider_id':2, '_IP':'10.0.1.14',
        #                        'protocol':'ssh', 'comment':'14'})
        # s.nodes.add(*[])
        saltapi.run_script('*', 'scripts/python/test.py')
        return Response({'OK':'ok'})