from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
import logging
from datetime import datetime

logger = logging.getLogger('devops')

try:
    scheduler = BackgroundScheduler()
    # scheduler.add_jobstore(DjangoJobStore(), 'default')
    # register_events(scheduler)
    scheduler.start()
    logger.info('apscheduler is running......')
except Exception as e:
    logging.error(e)
    scheduler.shutdown()

try:
    django_scheduler = BackgroundScheduler()
    django_scheduler.add_jobstore(DjangoJobStore(), 'default')
    register_events(django_scheduler)
    django_scheduler.start()
    logger.info('django apscheduler is running......')
except Exception as e:
    logging.error(e)
    django_scheduler.shutdown()


# 使用 django_apscheduler 调用此方法会导致无限循环
def scheduler_run_now(scheduler, *args, **kwargs):
    def wrapper(func):
        def inner(*a, **k):
            # kwargs.setdefault("id", "{}.{}".format(func.__module__, func.__name__))
            scheduler.add_job(func, *args, **kwargs, run_date=datetime.now(), args=a, kwargs=k)
        return inner
    return wrapper


def my_scheduler_run_now(*args, **kwargs):
    def wrapper(func):
        def inner(*a, **k):
            scheduler.add_job(func, *args, **kwargs, run_date=datetime.now(), args=a, kwargs=k)
        return inner
    return wrapper


