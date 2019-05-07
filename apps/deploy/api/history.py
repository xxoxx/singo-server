__author__ = 'singo'
__datetime__ = '2019/5/5 10:44 AM '


from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action
import linecache

from ..serializers import HistorySerializer
from ..models import History
from common.pagination import CustomPagination
from common.utils import logger

class HistoryViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = HistorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    # filter_class = DeploymentOrderFilter
    search_fields = ('title', 'project_name')
    ordering_fields = ('start',)
    pagination_class = CustomPagination
    queryset = History.objects.all()


    @action(detail=True, methods=['get'], name='history-log',
            url_path='log')
    def log(self, request, pk):
        try:
            obj = self.get_object()
            lineno = int(request.GET.get('lineno', 1))
            size = int(request.GET.get('size', 0))
            line_count = len(linecache.getlines(obj.log_file))

            if line_count == 0:
                return Response({'detail': '不存在日志文件或者日志文件无内容', 'is_tail': True}, status=status.HTTP_404_NOT_FOUND)
            elif line_count >= lineno:
                lines = linecache.getlines(obj.log_file)[lineno-1: lineno-1+size]
                is_tail = bool(line_count < (lineno+size))
                return Response({'content': lines, 'is_tail': is_tail})

        except Exception as e:
            logger.exception(e)
            logger.error(e)
            return Response({'detail': '获取日志失败'}, status=status.HTTP_400_BAD_REQUEST)