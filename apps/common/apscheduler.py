from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
import logging
from datetime import datetime
import time
from django.core.cache import cache

logger = logging.getLogger('devops')

try:
    scheduler = BackgroundScheduler(
        job_defaults={
            'max_instances': 1000,
            'misfire_grace_time': 60
        },
    )
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
# @scheduler_run_now(scheduler, 'date')
def scheduler_run_now(scheduler, *args, **kwargs):
    def wrapper(func):
        def inner(*a, **k):
            scheduler.add_job(func, *args, **kwargs, run_date=datetime.now(), args=a, kwargs=k)
        return inner
    return wrapper


def my_scheduler_run_now(*args, **kwargs):
    def wrapper(func):
        def inner(*a, **k):
            job_id = str(hash(time.time()))
            # cache.set('{}.{}'.format(func.__module__, func.__name__), job_id, timeout=60)
            k['job_id'] = job_id
            scheduler.add_job(func, id=job_id, run_date=datetime.now(), args=a, kwargs=k, *args, **kwargs)
        return inner
    return wrapper