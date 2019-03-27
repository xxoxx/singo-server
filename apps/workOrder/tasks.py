__author__ = 'singo'
__datetime__ = '2019/2/25 4:47 PM '

import logging
from common.utils import send_mail_common


logger = logging.getLogger('devops')


def send_process_order_mail(order):
    '''
    :param order:  工单对象
    :return:
    '''
    subject = '{}发起了工单申请'.format(order.applicant.name)
    recipient_list = [order.designator.email]
    message = '''
    【devops】:{}
    '''.format(order.contents)

    send_mail_common(subject=subject, message=message, recipient_list=recipient_list)
    # try:
    #     debug = settings.DEBUG
    #     email_from = settings.EMAIL_FROM
    #
    #     if debug:
    #         logger.debug(message)
    #     else:
    #         send_mail_async(subject, message, email_from, recipient_list)
    # except KeyError:
    #     logger.error('配置文件DEBUG,或者EMAIL_FROM值缺失')
    # except Exception as e:
    #     logger.error('发送邮件失败:', e)

def send_change_process_order_mail(current_user, order):
    subject = '{}向你分发了工单'.format(current_user.name)
    message = '''
        【devops】:{}
        '''.format(order.contents)
    recipient_list = [order.current_processor.email]

    send_mail_common(subject=subject, message=message, recipient_list=recipient_list)

def send_result_order_mail(order):
    subject = '工单处理结果'
    message = {
        2: '你的工单已处理完成, 登录平台查看详情',
        3: '你的工单已处理失败, 登录平台查看详情',
        4: '你的工单已被{}拒绝'.format(order.finally_processor.name)
    }[order.status]
    recipient_list = [order.applicant.email]

    send_mail_common(subject=subject, message=message, recipient_list=recipient_list)
