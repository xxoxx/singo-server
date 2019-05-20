import string
import random
import ipaddress
import requests
import logging
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache

from common.tasks import send_mail_async

User = get_user_model()
logger = logging.getLogger('devops')

# 随机数生成器
def id_generator(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def get_request_ip(request):
    '''
    获取request请求IP地址
    :param request:
    :return: ipaddress
    '''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')
    if x_forwarded_for and x_forwarded_for[0]:
        login_ip = x_forwarded_for[0]
    else:
        login_ip = request.META.get('REMOTE_ADDR', '')
    return login_ip

def validate_ip(ip):
    '''
    验证IP的合法性
    :param ip: ipaddress
    :return: Boll
    '''
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def get_ip_city(ip, timeout=10):
    # Taobao ip api: http://ip.taobao.com/service/getIpInfo.php?ip=8.8.8.8
    # Sina ip api: http://int.dpool.sina.com.cn/iplookup/iplookup.php?ip=8.8.8.8&format=json

    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip
    try:
        r = requests.get(url, timeout=timeout)
    except:
        r = None
    city = 'Unknown'
    if r and r.status_code == 200:
        try:
            data = r.json()
            if not isinstance(data, int) and data['code'] == 0:
                country = data['data']['country']
                _city = data['data']['city']
                if country == 'XX':
                    city = _city
                else:
                    city = ' '.join([country, _city])
        except ValueError:
            pass
    return city


def init_kwargs(model, **kwargs):
    '''
    去除字典中存着Model中不存着的字段
    :param Django model:
    :param kwargs:
    :return:
    '''
    return {
        k: v for k, v in kwargs.items() if k in [
           f.name for f in model._meta.get_fields()
        ]
    }

class Bcolor(object):
    '''
    终端输出颜色
    '''
    @staticmethod
    def color(code):
        def inner(text, bold=False):
            c = code
            if bold:
                c = '1;{}'.format(c)
            return '\033[{}m{}\033[0m'.format(c, text)
        return inner

    @staticmethod
    def red(text):
        return  Bcolor.color(31)(text)

    @staticmethod
    def b_red(text):
        return  Bcolor.color(41)(text)

    @staticmethod
    def yellow(text):
        return Bcolor.color(33)(text)

    @staticmethod
    def b_yellow(text):
        return Bcolor.color(43)(text)

    @staticmethod
    def green(text):
        return Bcolor.color(32)(text)

    @staticmethod
    def b_green(text):
        return Bcolor.color(42)(text)

def send_mail_common(subject, message, recipient_list):
    try:
        debug = settings.DEBUG
        email_from = settings.EMAIL_FROM

        if debug:
            logger.debug(message)
        else:
            send_mail_async(subject, message, email_from, recipient_list)
    except KeyError:
        logger.error('配置文件DEBUG,或者EMAIL_FROM值缺失')
    except Exception as e:
        logger.error('发送邮件失败:', e)


def update_cache_value(cache_name, old_val=None, timeout=24*3600, **kwargs):
    try:
        old_val = old_val or cache.get(cache_name)
        old_val.update(kwargs)
        cache.set(cache_name, old_val, timeout=timeout)
        return old_val
    except Exception as e:
        logger.exception(e)
        return False

def update_obj(order_obj, **kwargs):
    order_obj.__dict__.update(**kwargs)
    order_obj.save()