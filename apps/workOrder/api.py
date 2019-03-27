__author__ = 'singo'
__datetime__ = '2019/2/25 3:39 PM '


from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q

from .models import WorkOrder
from .serializers import WorkOrderSerializer
from common.pagination import CustomPagination
from common.utils import Bcolor, logger
from .tasks import send_process_order_mail, send_change_process_order_mail, send_result_order_mail
from .filters import WorkOrderFilter
from common.utils import User

class WorkOrderViewset(viewsets.ModelViewSet):
    '''
    get:
        /api/workorder/v1/workorder/?type={val},
        type=self 返回自己提交的工单,
        type=join 返回指派给我的工单,
        默认返回所有;
        /api/workorder/v1/workorder/choices/status/
        获取工单状态;
        /api/workorder/v1/workorder/choices/type/
        获取工单类型
    '''
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
    pagination_class = CustomPagination
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('title',)
    ordering_fields = ('applied',)
    filter_class = WorkOrderFilter

    def get_queryset(self):
        type = self.request.GET.get('action', None)
        user = self.request.user

        if self.request.user.is_superuser:
            questset = WorkOrder.objects.all()
        elif type == 'self':
            questset = WorkOrder.objects.filter(applicant=user)
        elif type == 'join':
            questset = WorkOrder.objects.filter(current_processor=user)
        else:
            questset = WorkOrder.objects.filter(Q(current_processor=user)|Q(applicant=user))

        return questset

    def create(self, request, *args, **kwargs):
        ret = super(WorkOrderViewset, self).create(request, *args, **kwargs)
        if ret.status_code == 201:
            # content = JSONRenderer().render(ret.data)
            # content = json.loads(content.decode('utf8'))
            pk = ret.data.get('id')
            instance = WorkOrder.objects.get(pk=pk)
            send_process_order_mail(instance)
        return ret

    def update(self, request, *args, **kwargs):
        switch = {
            'close': self.__close,
            'process': self.__processing,
            'reject': self.__reject,
            'distribution': self.__distribution,
            'complete': self.__complete,
            'default':'default'
        }
        self.request.POST._mutable = True
        _action = request.data.get('action', 'default')
        try:
            ret = switch.get(_action, 'default')(request, *args, **kwargs)
        except Exception as e:
            logger.critical(e)
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # instance = self.get_object()
        # old_processor_id = instance.current_processor.id
        # old_status = instance.status
        # ret = super(WorkOrderViewset, self).update(request, *args, **kwargs)
        # instance = self.get_object()  # 更新实例

        # # 当工单分发给其他人员时需要邮件通知
        # if instance.current_processor.id != old_processor_id:
        #     send_change_process_order_mail(self.request.user, instance)
        #
        # # 当工单的状态为失败、成功、拒绝的时候需要发送邮件通知工单发起人
        # if instance.status != old_status:
        #     if instance.status == 2 or instance.status == 3 or instance.status == 4:
        #         send_result_order_mail(instance)

        return ret

    def __get_choices(self, choices_type):
        choices = getattr(WorkOrder, choices_type)
        return dict(choices)

    # 处理工单
    def __processing(self, request, *args, **kwargs):
        request.data['status'] = 1
        ret = super(WorkOrderViewset, self).update(request, *args, **kwargs)
        return ret

    #拒绝工单
    def __reject(self, request, *args, **kwargs):
        request.data['status'] = 4
        # 最终处理人
        request.data['finally_processor'] = request.user.id
        ret = super(WorkOrderViewset, self).update(request, *args, **kwargs)
        instance = self.get_object()
        send_result_order_mail(instance)
        return ret

    # 关闭工单
    def __close(self, request, *args, **kwargs):
        request.data['status'] = 5
        ret = super(WorkOrderViewset, self).update(request, *args, **kwargs)
        return ret

    # 转发工单
    def __distribution(self, request, *args, **kwargs):
        ret = super(WorkOrderViewset, self).update(request, *args, **kwargs)
        instance = self.get_object()
        send_change_process_order_mail(self.request.user, instance)
        return ret

    # 完成工单
    def __complete(self, request, *args, **kwargs):
        # 最终处理人
        request.data['finally_processor'] = request.user.id
        request.data['status'] = 2
        ret = super(WorkOrderViewset, self).update(request, *args, **kwargs)
        instance = self.get_object()
        send_result_order_mail(instance)
        return ret

    @action(detail=False, methods=['get'], name='choices-status',
            url_path='choices/status', permission_classes=[permissions.IsAuthenticated])
    def get_choices_status(self, request):
        '''
        返回工单状态选择
        :param request:
        :return:
        '''
        try:
            data = self.__get_choices('STATUS')
        except Exception as e:
            logger.critical('获取工单状态选项失败')
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)

        return Response(data)

    @action(detail=False, methods=['get'], name='choices-type',
            url_path='choices/type', permission_classes=[permissions.IsAuthenticated])
    def get_choices_type(self, request):
        '''
        返回工单类型选择
        :param request:
        :return:
        '''
        try:
            data = self.__get_choices('TYPE')
        except Exception as e:
            logger.critical('获取工单类型选项失败')
            return Response({'detail': str(e)}, status=status.HTTP_404_NOT_FOUND)

        return Response(data)

from rest_framework import generics, viewsets, mixins
from common.permissions import DevopsPermission
class Test(viewsets.GenericViewSet):
    serializer_class = WorkOrderSerializer
    permission_classes = (permissions.IsAuthenticated, DevopsPermission,)
    perms_map = {
        'GET': ['{}.delete1'],
        'POST':['{}.delete'],
    }

    def list(self, request, *args, **kwargs):
        self.perms_map['GET'] = '{}.delete'
        print(Bcolor.green(self.perms_map))
        return Response({'detail':'赵永强尼玛'})

    @action(detail=False, methods=['get'], name='lemon',
            url_path='lemon', **{'perms_map':{'GET': ['{}.delete']}})
    def get_choices_type(self, request):
        print('sadasadas')
        return Response({'detail':'12113123'})


    def _post(self, request):
        from common.utils import Bcolor
        user  = User.objects.get(username='test')
        # print(user.has_perm('users.add_user'))
        perms_map = {
            'GET': [],
            'OPTIONS': [],
            'HEAD': [],
            'POST': ['%(app_label)s.add_%(model_name)s'],
            'PUT': ['%(app_label)s.change_%(model_name)s'],
            'PATCH': ['%(app_label)s.change_%(model_name)s'],
            'DELETE': ['%(app_label)s.delete_%(model_name)s'],
        }
        perms = [perm for perm in perms_map['POST']]
        print(Bcolor.green(perms))
        # print(Bcolor.red(user.has_perms(perms)))
        print(Bcolor.red(user.has_perms([])))
        return Response({'status': 'OK'})