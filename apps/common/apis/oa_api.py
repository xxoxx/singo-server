__author__ = 'singo'
__datetime__ = '2019/2/27 4:52 PM '

import requests
import json

from common.utils import logger
from django.conf import settings

class OAAPI(object):
    '''
    第三方接口用来获取用户信息
    '''

    def __init__(self, url, username, password, timeout=30):
        self.url = url
        self.username = username
        self.password = password
        self.timeout = timeout
        self.token = None

        # self.token = self.__get_token()
        self.token = '12b492b4-1044-4b26-adce-a8505f03d577'

    def get_token(self, prefix='token'):
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
            req = __request(**__params)

            if req.status_code == 401 and req.json().get('code') == '1010':
                self.token = self.get_token()
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


oaapi = OAAPI(url=settings.OAAPI.get('URL'),
              username=settings.OAAPI.get('USERNAME'),
              password=settings.OAAPI.get('PASSWORD'),
              timeout=30)
