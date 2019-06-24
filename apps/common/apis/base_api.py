__author__ = 'singo'
__datetime__ = '2019/2/27 4:54 PM '

import requests
import urllib3
import time
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger('devops')


class BaseAPI(object):
    def __init__(self, url, username, password, timeout=30):
        self.url = url
        self.username = username
        self.password = password
        self.timeout = timeout
        self.token_expire = None
        self.token = None

    def get_token(self):
        pass
