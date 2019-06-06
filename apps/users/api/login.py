__author__ = 'singo'
__datetime__ = '2019/2/21 3:15 PM '

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from ..tasks import write_login_log
from ..tasks import set_last_login
from common.apis import oaapi
from common.utils import logger


jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
User = get_user_model()

def os_userinfo(username):
    userinfo = oaapi.get_userinfo(username)
    logger.info(userinfo)
    data = {}
    if userinfo:
        data = {
            'username': userinfo.get('loginName'),
            'name': userinfo.get('name'),
            'email': userinfo.get('emailAddress') if userinfo.get('emailAddress') else '{}@cwst.com'.format(username),
            'phone': userinfo.get('telNumber')
        }

    return data

def oa_login(f):
    def inner(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        #验证OA中的账号
        if oaapi.user_auth(username, password):
            logger.info('OA账号:{},{}'.format(username, password))
            try:
                # 从本地读取或者创建账号
                user = User.objects.get_or_create(username=username, defaults=os_userinfo(username))[0]
                # 从OA同步密码
                if not user.check_password(password):
                    user.set_password(password)
                    user.save()
            except Exception as e:
                logger.critical(str(e))

        return f(self, request, *args, **kwargs)
    return inner

class ObtainAuthTokenAndLogging(ObtainAuthToken):
    '''
    获取用户token并记录日志
    '''
    def post(self, request, *args, **kwargs):
        try:
            username = request.data['username']
            ret = super(ObtainAuthTokenAndLogging, self).post(request, *args, **kwargs)
        except Exception as e:
            ret = None
            return Response({'detail': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
        finally:
            write_login_log(request, username=username, status=bool(ret), type='TOKEN')

        set_last_login(username)
        return ret

class obtainJwtTokenAndLogging(ObtainJSONWebToken):
    # 获取用户JWT的token并记录日志
    @oa_login
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)

            set_last_login(username)
            write_login_log(request, username=username, status=True, type='JWT')
            return response

        else:
            logger.info(serializer.errors)
            write_login_log(request, username=username, status=False, type='JWT')
            return Response({'detail': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.decorators import api_view, permission_classes
# VPN授权登录验证
# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def OAAuthWithForVPN(request):
#
#     username = request.data.get('username')
#     password = request.data.get('password')
#
#     data = {
#         "status": 1,
#         "userinfo": {
#             "usergroup": "undefine",
#             "username": username,
#             "usernote": "undefine"
#         }
#     }
#
#     if oaapi.user_auth(username, password):
#         logger.info('OA账号:{},{}'.format(username, password))
#         user_info = oaapi.get_userinfo(username)
#
#         data = {
#             "status": 0,
#             "userinfo": {
#                 "usergroup": user_info.get('orgDepartmentName'),
#                 "username": username,
#                 "usernote": user_info.get('orgPostName')
#             }
#         }
#
#
#     return Response(data)

