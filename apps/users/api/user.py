from rest_framework import status, viewsets, mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
import json

from ..serializers import UserUpdateGroupSerializer, ChangeUserPasswordSerializer
from ..models import User
from ..serializers import UserSerializer, UserRegistSerializer
from ..filters import UserProfileFilter
from common.pagination import CustomPagination
from common.permissions import IsSuperuserOrSelf
from common.permissions import DevopsPermission
from common.utils import logger

class UserProfileViewSet(mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, DevopsPermission)
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UserProfileFilter
    search_fields = ('username', 'name')
    ordering_fields = ('username', 'id')
    pagination_class = CustomPagination
    queryset = User.objects.filter()

    perms_map = {
        'GET': [],
        'POST': ['{}.user_add'],
        'PUT': ['{}.user_edit'],
        'PATCH': ['{}.user_edit'],
        'DELETE': ['{}.user_delete']
    }

    def list(self, request, *args, **kwargs):
        self.queryset = User.objects.filter(is_superuser=0).exclude(username=request.user.username)
        return super(UserProfileViewSet, self).list(request, *args, **kwargs)

    @action(detail=False, methods=['get'], name='user-info', url_path='user-info')
    def userInfo(self, request):
        """
        获取当前登陆的用户信息
        """
        serializer = UserSerializer(self.request.user)
        uri = request.build_absolute_uri('/').strip("/")
        data = serializer.data
        data['avatar'] = uri + data['avatar'] if data['avatar'] else uri +'/media/avatar/plane.jpg'
        data['permissions'] = request.user.get_all_permissions()
        data['properties'] = json.loads(data['properties'])

        return Response(data)


class  UserRegistAPIView(generics.CreateAPIView):
    '''
    用户注册

    post:
    用户注册
    '''
    serializer_class = UserRegistSerializer


class ChangeUserPasswordViewSet(mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    '''
    修改用户密码
    '''
    queryset = User.objects.all()
    serializer_class = ChangeUserPasswordSerializer
    permission_classes = (IsSuperuserOrSelf, DevopsPermission)

    perms_map = {
        'PUT': ['{}.change_password'],
        'PATCH': ['{}.change_password'],
    }

    '''
    修改密码有问题,在serializer里修改无法进行权限控制
    '''

    @action(detail=True, methods=['put', 'patch'], name='Rest Password',
            url_path='rest', permission_classes=[permissions.IsAuthenticated, DevopsPermission],
            **{'perms_map': {'PUT': ['{}.reset_password'], 'PATCH': ['{}.reset_password']}})
    def rest_password(self, request, pk=None):
        '''
        重置用户密码
        '''
        from common.utils import id_generator as password_generator
        from ..utils import send_user_rest_password_mail
        user = self.get_object()
        password = password_generator()
        user.set_password(password)
        user.save()
        user.password = password
        send_user_rest_password_mail(user)
        return Response({'detail':'修改密码成功'}, status=200)

class UserUpdateGroupApi(generics.UpdateAPIView):
    '''
    put: 更新用户所在组
    '''
    perms_map = {
        'PUT': ['{}.user_group_change'],
        'PATCH': ['{}.user_group_change'],
    }

    queryset = User.objects.all()
    serializer_class = UserUpdateGroupSerializer
    permission_classes = (permissions.IsAuthenticated, DevopsPermission)


'''
class UserChangePasswordAPI(generics.RetrieveUpdateAPIView):
    # queryset = UserProfile.objects.all()
    # serializer_class = ChangeUserPasswordSerializer

    def get_queryset(self):
        print(self.request.user)
        return UserProfile.objects.all()

    def perform_update(self, serializer):
        user = self.get_object()
        user.password_raw = serializer.validated_data['password']
        user.save()
'''

'''
class UserChangePasswordViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = request.user
        serializer = ChangeUserPasswordSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        from django.shortcuts import get_object_or_404
        queryset = UserProfile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ChangeUserPasswordSerializer(user)
        return Response(serializer.data)

    @action(detail=True, methods=['put'], name='Change Password')
    def set_password(self, request, pk=None):
        print('=============')
        if(pk.replace('-', '') != str(request.user.id).replace('-', '')):
            return Response({'detail:' '只能修改登录用户密码'},status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        serializer = ChangeUserPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': '密码修改成功'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


