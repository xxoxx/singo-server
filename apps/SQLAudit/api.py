__author__ = 'singo'
__datetime__ = '2019/4/17 2:08 PM '

from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from pymongo import DESCENDING

from common.apis import mongodb_client
from common.utils import logger
from common.permissions import DevopsPermission



class NodesAPI(APIView):
    permission_classes = (permissions.IsAuthenticated, DevopsPermission)

    perms_map = {
        'GET': ['{}.SQLAudit_list']
    }

    def get(self, request, format=None):
        try:
            databases = [db for db in mongodb_client.list_database_names() if 'audit' in db]
            # data = [{db: mongodb_client[db].collection_names()} for db in databases]
            data = [{'db': db, 'tables': mongodb_client[db].collection_names()} for db in databases]
        except Exception as e:
            logger.error(e)
            return Response({'detail': str(e)})
        return Response(data)


class DocumentsAPI(APIView):
    permission_classes = (permissions.IsAuthenticated, DevopsPermission)

    perms_map = {
        'GET': ['{}.SQLAudit_list']
    }

    def get(self, request, format=None):
        # 2019-04-17 00:00:00
        try:
            data = request.GET

            # 查询条件
            datetime_start = data.get('datetime_start')
            datetime_end = data.get('datetime_end')
            db_name = data.get('db_type')
            collection_name = data.get('db_instance')
            accountName = data.get('account_name', '.*')
            sql_text ='.*{}.*'.format(data.get('cmd')) if data.get('cmd') else '.*'

            # 分页
            page = int(data.get('page', 1))
            size = int(data.get('size', 10))

            skip_count = (page-1) * size
            collection = mongodb_client[db_name][collection_name]
            cursor = collection.find({'ExecuteTime':{'$gte': datetime_start,
                                                     '$lte': datetime_end},
                                      'AccountName':{'$regex': accountName},
                                      'SQLText': {'$regex': sql_text}}).sort('ExecuteTime', DESCENDING)
            # 分页后的数据
            documents = list(cursor.skip(skip_count).limit(size))
            print(len(documents))
            # 转换MongoDBObjectId
            for i in range(len(documents)):
                documents[i]['_id'] = str(documents[i]['_id'])

            data = {
                'count': cursor.count(),
                'results': documents
            }

            return Response(data)

        except (ValueError, TypeError) as e:
            logger.info(e)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(e)
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)