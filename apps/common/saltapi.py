import logging

# from saltManagement.saltapi import SaltAPI
# from devops.settings import SALTAPI
from django.conf import settings
import requests
import urllib3
import time
import logging
from common.utils import Bcolor

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger('devops')

class SaltAPI(object):
    def __init__(self, url, username, password, timeout=30):
        self.__url = url
        self.__username = username
        self.__password = password
        self.__timeout = timeout
        # self.__token_expire = None
        self.__token_expire = 1645834300.495736
        self.__token = '0d75285468a0a8b092daf77896eda41cfeb055bb'
        # self.__token = self.get_token()
        print('\033[93msalt api Token: 0d75285468a0a8b092daf77896eda41cfeb055bb\033[0m')

    def get_token(self, prefix='/login'):
        """
        登录获取token
        """
        data = {
            "username": self.__username,
            "password": self.__password,
            "eauth": "pam"
        }
        headers = {
            'Accept': 'application/json'
        }
        loginurl = '{}{}'.format(self.__url, prefix)

        try:
            req = requests.post(loginurl, headers=headers,
                                data=data, verify=False, timeout=self.__timeout)
            token = req.json()['return'][0]['token']
            self.__token_expire = req.json()['return'][0]['expire']
            logger.debug('获取 salt-api Token:{}'.format(token))

            return token
        except KeyError:
            logger.critical('获取 sal-api Token 失败')
            raise KeyError
        except Exception as e:
            logger.critical('登录 salt-api 失败')
            raise e

    def post(self, prefix='/', **data):
        headers = {
            'Accept': 'application/json',
            'X-Auth-Token': self.__token
        }
        # token 过期,重新获取
        if not self.__token_expire > time.time():
            self.__token = self.get_token()
            self.__header["X-Auth-Token"] = self.__token

        url = '{}{}'.format(self.__url, prefix)

        try:
            req = requests.post(url, data=data, headers=headers, verify=False, timeout=self.__timeout)
        except Exception as e:
            logger.error('连接salt api失败')
            logger.error(e)
            raise e
        return req

    def get(self, prefix='/', **data):
        headers = {
            'Accept': 'application/json',
            'X-Auth-Token': self.__token
        }
        # token 过期,重新获取
        if not self.__token_expire > time.time():
            self.__token = self.get_token()
            self.__header["X-Auth-Token"] = self.__token

        url = '{}{}'.format(self.__url, prefix)

        try:
            req = requests.get(url, params=data, headers=headers, verify=False, timeout=self.__timeout)
        except Exception as e:
            logger.error('连接salt api失败')
            logger.error(e)
            raise e
        return req

    def __handle_key_response(self, action, **data):
        try:
            req = self.post(**data)
            logger.debug(req.json())

            if req.status_code != 200:
                response =  {'code': req.status_code, 'detail': '请求异常'}
            else:
                _data = req.json()
                # salt-api 返回的状态
                status = _data['return'][0]['data']['success']
                # salt-api 返回执行成功的成员,任意saltID都会返回status,最终结果还得看numbers
                numbers = _data['return'][0]['data']['return']
                if numbers and status:
                    response = {
                        'code':200,
                        'status':status,
                        'detail':'{}成功'.format(action)
                    }
                else:
                    if not status:
                        response = {'code': 200, 'status': status, 'detail':'{}失败'.format(action)}
                    else:
                        response = {
                            'code': 200,
                            'status': False,
                            'detail':'未知的minion'
                        }
        except KeyError:
            logger.error('数据解析错误')
            logger.error(req.text)
            response = {'code': -1, 'detail': '不能解析salt返回的数据'}
        except Exception as e:
            logger.error(e)
            response =  {'code': -1, 'detail': 'salt api返回数据异常'}

        return response

    def key_list(self):
        data = {
            'client': 'wheel',
            'fun': 'key.list_all'
        }
        try:
            req = self.post(**data)
            if req.status_code != 200:
                response = {'code': req.status_code, 'detail':'请求异常'}
            else:
                _data = req.json()
                ret = _data['return'][0]['data']['return']
                response = {
                    'minions_rejected': ret['minions_rejected'],
                    'minions_denied': ret['minions_denied'],
                    'minions_pre': ret['minions_pre'],
                    'minions': ret['minions'],
                    'code': 200
                }
        except KeyError:
            logger.error('数据解析错误')
            logger.error(req.text)
            response = {'code': -1, 'detail': '不能解析salt返回的数据'}
        except Exception as e:
            logger.error(e)
            response = {'code': -1, 'detail': 'salt api未返回数据'}
        return response

    def accept_key(self, key_id):
        data = {
            'client': 'wheel',
            'fun': 'key.accept',
            'match': key_id,
            'include_rejected': True,
            'include_denied': True
        }
        # try:
        #     req = self.post(**data)
        #     logger.debug(req.json())
        #
        #     if req.status_code != 200:
        #         response =  {'code': req.status_code, 'detail': '请求异常'}
        #     else:
        #         _data = req.json()
        #         # salt-api 返回的状态
        #         status = _data['return'][0]['data']['success']
        #         # salt-api 返回执行成功的成员,任意saltID都会返回status,最终结果还得看numbers
        #         numbers = _data['return'][0]['data']['return']
        #         if numbers and status:
        #             response = {
        #                 'code':200,
        #                 'status':status,
        #                 'detail':'接受key成功'
        #             }
        #         else:
        #             if not status:
        #                 response = {'code': 200, 'status': status, 'detail':'授权key失败'}
        #             else:
        #                 response = {
        #                     'code': 200,
        #                     'status': False,
        #                     'detail':'未找到key id为{}的minion'.format(key_id)
        #
        #                 }
        # except KeyError:
        #     logger.error('数据解析错误')
        #     logger.error(req.text)
        #     response = {'code': -1, 'detail': '不能解析salt返回的数据'}
        # except Exception as e:
        #     logger.error(e)
        #     response =  {'code': -1, 'detail': 'salt api未返回数据'}

        return self.__handle_key_response('授权', **data)

    def delete_key(self, key_id):
        data = {
            'client': 'wheel',
            'fun': 'key.delete',
            'match': key_id
        }

        try:
            req = self.post(**data)
            logger.debug(req.json())

            if req.status_code != 200:
                response =  {'code': req.status_code, 'detail': '请求异常'}
            else:
                _data = req.json()
                # salt-api 返回的状态
                status = _data['return'][0]['data']['success']
                response = {
                    'code': 200,
                    'status': status,
                    'detail': '删除key成功'
                }
                # delete key 无论key是否存在都返回空
                # numbers = _data['return'][0]['data']['return']
                if not status:
                    response['detail'] = '删除key失败'
        except KeyError:
            logger.error('数据解析错误')
            logger.error(_data)
            response = {'code': -1, 'detail': '不能解析salt返回的数据'}
        except Exception as e:
            logger.error(e)
            response =  {'code': -1, 'detail': 'salt api未返回数据'}

        return response

    def reject_key(self, key_id):
        """
        驳回
        :param key_id:
        :return:
        """
        data = {
            'client': 'wheel',
            'fun': 'key.reject',
            'include_accepted': True,
            'include_denied': True
        }

        return self.__handle_key_response('驳回', **data)

    def deny_key(self, key_id):
        pass

    def get_grains_items(self, key_id):
        prefix = '/minions/{}'.format(key_id)
        try:
            req = self.get(prefix=prefix)
            logger.debug(req.json())
            if req.status_code != 200:
                response =  {'code': req.status_code, 'detail': '请求异常'}
            else:
                _data = req.json()
                response = _data['return'][0][key_id]
                response['code'] = 200
        except KeyError:
            logger.error(_data)
            response = {'code': -1, 'detail': '不能解析salt返回的数据'}
        except Exception as e:
            logging.error(e)
            response = {'code': -1, 'detail': 'salt api返回数据异常'}
        return response

    def run_script(self, tgt, path):
        data = {
            'client': 'local',
            'fun': 'cmd.script',
            'tgt': tgt,
            'arg': 'salt://'+ path
        }
        req = self.post(**data)

        if req.status_code != 200:
            response = {'code': req.status_code, 'detail': req.text}
        else:
            response = req.json().get('return', req.json())
        return response


try:
    url = settings.SALTAPI.get('URL')
    username = settings.SALTAPI.get('USERNAME')
    password = settings.SALTAPI.get('PASSWORD')
    saltapi = SaltAPI(url=url, username=username, password=password)
    # saltapi.run_script('devops', 'scripts/python/test.py')
    # print(saltapi.post(**{'client': 'wheel', 'fun': 'key.list_all'}))
except KeyError:
    logger.critical('获取salt配置失败')
    raise KeyError
except Exception as e:
    logger.critical(e)