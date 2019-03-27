from django.core.exceptions import ObjectDoesNotExist
import logging

from common.utils import validate_ip, get_ip_city
from .models import LoginLog, User
from common import scheduler
from common.apscheduler import scheduler_run_now

logger = logging.getLogger('devops')

# def write_login_log_async(*args, **kwargs):
#     '''
#     用户登录日志
#     '''
#     ip = kwargs.get('ip')
#     if not(ip and validate_ip(ip)):
#         ip = ip[:15]
#         city = 'Unknown'
#     else:
#         city = get_ip_city(ip)
#
#     kwargs.update({'ip':ip, 'city': city})
#     LoginLog.objects.create(**kwargs)


@scheduler_run_now(scheduler, 'date')
def set_last_login(username):
    from django.utils import timezone
    try:
        user = User.objects.get(username=username)
        user.last_login = timezone.now()
        if user.is_first_login: user.is_first_login = False
        user.save()
    except ObjectDoesNotExist:
        logger.warning('更新登录时间失败')

@scheduler_run_now(scheduler, 'date')
def write_login_log(request, username=None, status=False, type=None):
    from common.utils import get_request_ip
    login_ip = get_request_ip(request)
    agent = request.META.get('HTTP_USER_AGENT')

    if not (login_ip and validate_ip(login_ip)):
        login_ip = login_ip[:15]
        city = 'Unknown'
    else:
        city = get_ip_city(login_ip)

    data = {
        'username': username,
        'type': type,
        'ip': login_ip,
        'agent': agent,
        'status': status,
        'city': city
    }

    LoginLog.objects.create(**data)
    # scheduler.add_job(write_login_log_async, 'date',
    #                   run_date=datetime.now(),
    #                   kwargs=data)

