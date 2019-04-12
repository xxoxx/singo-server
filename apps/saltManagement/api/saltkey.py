from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.validators import ValidationError

from common.apis import saltapi
from common.permissions import IsSuperuser
from common.utils import logger
from resources.createSources.server import saveServer

class SaltKeyAPI(APIView):
    '''
    salt key管理

    get:
        获取key列表

    post:
        接受一个key

    patch:
        拒绝一个key

    delete:
        删除一个key
    '''
    permission_classes = (IsSuperuser,)

    def get(self, request, format=None):
        data = saltapi.key_list()
        return Response(data)

    def post(self, request, format=None ):
        salt_id = request.data.get('keyID')
        response = saltapi.accept_key(salt_id)

        if response.get('code') == 200 and request.data.get('addAssets'):
            data = saltapi.get_grains_items(salt_id)
            try:
                if data['code'] == 200:
                    data['comment'] = '来自salt添加'
                    saveServer(data)
            except ValidationError as e:
                logger.error(e)
                response['detail'] = '接受KEY成功,资产中已存在此saltID的资产'
            except Exception as e:
                logger.error(e)
                response['detail'] = '接受KEY成功,导入到资产失败'
        # response = {'code': 200, 'status': True, 'detail': '接受KEY成功,资产中已存在此saltID的资产'}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        data = saltapi.reject_key(request.data.get('keyID'))
        return Response(data)

    def delete(self, request, *args, **kwargs):
        data = saltapi.delete_key(request.data.get('keyID'))
        return Response(data)

class Test(APIView):
    def get(self, request, format=None):
        data = saltapi.get_grains_items('devops')

        print('===========================')
        data['comment'] = '来自salt添加'
        if data['code'] == 200:
            try:
                data = saveServer(data)
            except ValidationError as e:
                print(e)
                print('赵永强你麻痹')
            except Exception as e:

                print(e)
                print('我抓住你了')

        print(data)
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
        # saltapi.run_script('*', 'scripts/python/test.py')
        return Response({'OK':'ok'})