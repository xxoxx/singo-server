__author__ = 'singo'
__datetime__ = '2019/5/6 3:16 PM '

import requests
import json
from django.conf import settings

from common.utils import logger

class DingtalkChatbot(object):
    def __init__(self):
        self.webhook = settings.DINGTALK_CHATBOT.get('URI')
        self.headers = {'content-type': 'application/json', 'charset': 'utf-8'}


    def text_msg(self, content, at_mobiles=[], at_all=False):
        """
        # text类型
        :param content: 发送内容
        :param at_mobiles: @人的手机号
        :param at_all:  @所有人时：true，否则为false
        :return:
        """
        data = {
            'msgtype': 'text',
            'text': {
                "content": content
            },
            'at': {
                'atMobiles': at_mobiles,
                'isAtAll': at_all
            }
        }

        self.__post(data)


    def __post(self, data):
        try:
            ret = requests.post(self.webhook, data=json.dumps(data), headers=self.headers)
            if ret.json().get('errcode') != 0:
                raise Exception('钉钉机器人发送消息失败')
        except Exception as e:
            logger.exception(e)
            logger.error(e)



dingtalk_chatbot = DingtalkChatbot()