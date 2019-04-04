__author__ = 'singo'
__datetime__ = '2019/2/27 4:52 PM '

import requests
import json

from .base_api import BaseAPI
from common.utils import logger, Bcolor
from django.conf import settings

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
    oaapi = OAAPI(url=settings.OAAPI.get('URL'),
                  username=settings.OAAPI.get('USERNAME'),
                  password=settings.OAAPI.get('PASSWORD'),
                  timeout=30)
    # print(oaapi.user_auth(username='000214', password='nj532680'))
    # print(oaapi.get_userinfo(username='000214'))


