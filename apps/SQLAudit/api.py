__author__ = 'singo'
__datetime__ = '2019/4/17 2:08 PM '

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

from common.apis import mongodb_client
from common.utils import logger


class NodesAPI(APIView):
    def get(self, request, format=None):
        try:
            databases = [db for db in mongodb_client.list_database_names() if 'audit' in db]
            data = [{db: mongodb_client[db].collection_names()} for db in databases]
        except Exception as e:
            logger.error(e)
            return Response({'detail': str(e)})
        return Response(data)

    # def post(self, request, format=None):
        # client = MongoClient('mongodb://dba:dba@172.16.102.31:27017/')
        # db = client['audit_mysql']
        # collection = db['mysql_172.16.102.113']
        # cur = collection.find({'ip':'172.16.102.215'}).limit(4)
        # print(cur.count(with_limit_and_skip=True))
        # print(len(list(cur)))
        # print(cur[0])
        # next(cur)
        # print(cur[0])
        # print(list(next(cur) for _ in range(5)))
        # print(cur[3])
        # cur[3]['_id'] =
        # print(cur[3]['_id'])
        # cur = list(cur)
        # for i in range(len(cur)):
        #     cur[i]['_id'] = str(cur[i]['_id'])

        # s = '2019-04-15 00:00:00'
        # d = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
        # collection = mongodb_client['audit_mysql']['rds_rm_wz9szm691x24f9o40']
        # # collection = mangodb_client['audit_mysql']['mysql_172.16.102.113']
        # print('====')
        # print(collection.find({'ExecuteTime': {'$gte': d}}).count())
        # # print(collection.find().count())
        # print(collection.find()[0])
        # return Response('OK')


class DocumentsAPI(APIView):
    def get(self, request, format=None):
        try:
            data = request.GET
            page = int(data.get('page', 1))
            size = int(data.get('size', 10))
            datetime_start = data.get('datetime_start')
            datetime_end = data.get('datetime_end')
            db_name = data.get('db_type')
            collection_name = data.get('db_instance')

            collection = mongodb_client[db_name][collection_name]
            print('=============')
            print(collection.name)
            collection.find({'ExecuteTime':{'$gte': datetime_start}})

        except (ValueError, TypeError) as e:
            logger.info(e)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response('OK')