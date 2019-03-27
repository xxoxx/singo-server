import logging
from django.conf import settings

from common.tasks import send_mail_async

logger = logging.getLogger('devops')

def send_user_created_mail(user):
    subject = '用户开通'
    recipient_list = [user.email]
    message = '''
    【devops】：你在devops注册成功，用户名：{}，初始密码：{}，请请尽快登录平台修改密码。
    '''.format(user.username, user.password)

    if settings.DEBUG:
        logger.debug(message)
    else:
        send_mail_async(subject, message, '18058418418@189.cn', recipient_list)
        # scheduler.add_job(send_mail_async, 'date',
        #                   run_date=datetime.now(),
        #                   args=[subject, message, '18058418418@189.cn', recipient_list])

def send_user_rest_password_mail(user):
    subject = '密码重置'
    recipient_list = [user.email]
    message = '''
    【devops】：你的密码已被管理员重置， 新密码：{}，请请尽快登录平台修改密码。
    '''.format(user.password)

    if settings.DEBUG:
        logger.debug(message)
    else:
        send_mail_async(subject, message, '18058418418@189.cn', recipient_list)

