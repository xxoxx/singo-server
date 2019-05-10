__author__ = 'singo'
__datetime__ = '2019/5/6 3:16 PM '

import requests
import json
from django.conf import settings

from common.utils import logger

class DingtalkChatbot(object):
    def __init__(self):
        self.__webhook = settings.DINGTALK_CHATBOT.get('URI')
        self.__headers = {'content-type': 'application/json', 'charset': 'utf-8'}


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

    def send_link(self, title, text, message_url, pic_url='', msgtype='link',):
        """
        :param msgtype:     消息类型，此时固定为：link
        :param title:       消息标题
        :param text:        消息内容。如果太长只会部分展示
        :param message_url: 点击消息跳转的URL
        :param pic_url:     图片URL
        :return:
        """
        data = {
            "msgtype": msgtype,
            "link": {
                "text": text,
                "title": title,
                "messageUrl": message_url,
                "picUrl": pic_url
            }
        }
        self.__post(data)

    def __post(self, data):
        try:
            ret = requests.post(self.__webhook, data=json.dumps(data), headers=self.__headers)
            if ret.json().get('errcode') != 0:
                raise Exception('钉钉机器人发送消息失败')
        except Exception as e:
            logger.exception(e)


dingtalk_chatbot = DingtalkChatbot()