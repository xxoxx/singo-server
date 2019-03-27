__author__ = 'singo'
__datetime__ = '2019/2/27 4:52 PM '

import requests
import json

from .baseApi import BaseAPI
from common.utils import logger, Bcolor
from django.conf import settings

CODE = {
    '1001': 'exceed_max_member	超出并发数限制	超出了最大登录人数',
	'1002': 'exceed_max_member_in_account	超出单位并发数限制	超出了您所在单位的最大登录人数',
	'1003': 'loginUserState.adminKickoff	被管理员强制下线	您被管理员强制下线',
    '1004':	'LoginOfflineOperation.networkOff	网路故障	网络故障，您被迫下线',
    '1005':	'loginUserState.changePassword	其他端修改了密码	密码已被修改{0}，请重新登录',
    '1006':	'loginUserState.kickOff	被其他端下线	您的账号已被下线!',
    '1007':	'LoginOfflineOperation.loginAnotherone	在另一个地点登录,您的帐号在另一地点登录，您被迫下线',
    '1010':	'loginUserState.unknown	未知错误	被迫下线，原因：与服务器失去连接',
    '1021':	'无效的用户名或密码',
    '1022':	'无效的用户名或密码 该帐号仅剩下{0}次登录尝试机会',
    '1023':	'账号被锁定，请稍后重试或联系管理员',
    '1024':	'该帐号已经被禁用.请联系管理员',
    '1031':	'您没有在符合的IP范围内登录',
    '1041':	'管理员不能在该浏览器上登录',
    '1042': '管理员不能登录',
    '1045':	'短信登录验证码不匹配或过期',
    '1047':	'身份验证狗不可用',
    '1051':	'证书已过期',
    '1052':	'证书已吊销',
    '1053':	'证书被吊销且已过期',
    '1054':	'证书服务器错误，请联系管理员',
    '1055':	'证书与协同账号没有绑定，请联系管理员',
    '1056':	'此IP登录必须拥有账号所对应的CA证书',
    '1057':	'请安装CA证书或插入CA硬件设备，请联系管理员',
    '1058':	'此帐号和CA帐号绑定不正确，请联系管理员',
    '1060': '域用户验证失败',
    '1061':	'域用户验证失败'
}



class OAAPI(BaseAPI):

    def __init__(self, url, username, password, timeout=30):
        super(OAAPI, self).__init__(url=url, username=username, password=password, timeout=timeout)
        # self.token = self.__get_token()
        self.token = '355df79c-5861-47a9-8f99-0a7e3d7477ce'

    def __get_token(self, prefix='token'):
        """
        登录获取token
        """
        data = json.dumps({ "userName": self.username, "password": self.password})
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        token_url = '{}{}'.format(self.url, prefix)

        try:
            req = requests.post(token_url, headers=headers,
                                data=data, verify=False, timeout=self.timeout)
            if req.status_code == 200:
                logger.info('获取OA token: {}'.format(req.json()))
                return req.json().get('id')
        except Exception as e:
            logger.error(e)

        return ''

    def __oa_request(self, prefix='', type='get', **data):
        headers = { 'Accept': 'application/json' }
        url = '{}{}'.format(self.url, prefix)
        params = { 'token': self.token }

        if 'post' == type.lower():
            __params = {
                'headers': headers,
                'url': url,
                'params': params,
                'timeout': self.timeout,
                'json':  data,
                'verify': False
            }
            __request = requests.post
        else:
            __params = {
                'headers': headers,
                'url': url,
                'params': data,
                'timeout': self.timeout,
                'verify': False
            }
            __request = requests.get
        try:
            # req = requests.post(url=url, json=data, headers=headers, params=params,
            #                     verify=False, timeout=self.timeout)
            # req = requests.get(url, params=data,
            #                    headers=headers, verify=False, timeout=self.timeout)
            req = __request(**__params)

            if req.status_code == 401 and req.json().get('code') == '1010':
                self.token = self.__get_token()
                __params['params']['token'] = self.token
                req = __request(**__params)
            return req.json()
        except Exception as e:
            logger.error(e)

        return False

    def user_auth(self, username, password):
        data = {
            'username': username,
            'password': password,
            'token': self.token
        }
        return self.__oa_request(prefix='userAuth/userAuth/', type='post', **data)

    def get_userinfo(self, username):
        data = {
            'loginName': username,
            'token': self.token
        }

        return self.__oa_request(prefix='orgMember', type='get', **data)


if not settings.DEBUG:
    oaapi = None
else:
    url = settings.OAAPI.get('URL')
    username = settings.OAAPI.get('USERNAME')
    password = settings.OAAPI.get('PASSWORD')
    oaapi = OAAPI(url=url, username=username, password=password, timeout=30)
    # print(oaapi.user_auth(username='000214', password='nj532680'))
    # print(oaapi.get_userinfo(username='000214'))


