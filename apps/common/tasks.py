from django.core.mail import send_mail
from common.apscheduler import scheduler_run_now

@scheduler_run_now('date')
def send_mail_async(*args, **kwargs):
    send_mail(*args, **kwargs)