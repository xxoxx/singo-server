
import time

def show_time_1(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print(end_time-start_time)
    return inner

@show_time_1
def test_1():
    print('test_1')
    time.sleep(2)

# test_1()

#------------------------------------------
def show_time_2(f):
    def inner(*agrs, **kwargs):
        start_time = time.time()
        f()
        print(agrs)
        print(**kwargs)
        end_time = time.time()
        print(end_time-start_time)
    return inner

@show_time_2
def test_2():
    print('test_2')
    time.sleep(2)

# test = show_time(test, 'hello world')
# test_2('hello world')
# test_2('hello', 'world')


#------------------------------------------
def show_time_3(f):
    def inner(*agrs, **kwargs):
        start_time = time.time()
        f(agrs, kwargs)
        print(agrs)
        print(kwargs)
        end_time = time.time()
        print(end_time-start_time)
    return inner

@show_time_3
def test_3(*agrs, **kwargs):
    print('test_3')
    time.sleep(2)

# test_3('lemon', 'mango')


#------------------------------------------
def logger(falg=True):
    def show_time_4(f):
        print('show_time_4 -->1')
        def inner(*agrs, **kwargs):
            print('inner')
            start_time = time.time()
            f(agrs, kwargs)
            print(agrs)
            print(kwargs)
            end_time = time.time()
            print(end_time-start_time)
            print(falg)
        f('赵永强')
        print('show_time_4 -->2')
        return inner
    return show_time_4

# @logger(falg=False)
def test_4(*args, **kwargs):
    print('test_4')
    print(args)
    time.sleep(2)
# test_4('lemon', 'mango')
# test_4('lemon', 'mango')


def add(f):
    print('func')
    f('赵')

def register_job(scheduler, *a, **k):
    def test(func):
        print('scheduler')
        bbb=5
        def inner(*args,**kwargs):
            print('=======')
            add(func)
            # func()
            # scheduler.add_job(func, *a, **k)
            print(bbb)
            return func
        return inner
    return test



@register_job(True, a=1)
def show(name):
    print('test')
    print(name)

# show('zzz')(111)


def decorator(flag=None):
    def func1(f):
        def inner(*args,**kwargs):
            print('start inner')
            print('falg:%s'%flag)
            f(*args,**kwargs)
            print('end inner')
        return inner
    return func1

@decorator('lemon')
def foo(*args, **kwargs):
    print(sum(args))
    print('foo')

def test():
    print('zzz')

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

scheduler.add_job(test,  "interval", seconds=10)

scheduler.start()

from datetime import datetime
def register_job(scheduler, *args, **kwargs):
    def wrapper(func):
        def inner(*a, **k):
            print(a, k)
            # kwargs.setdefault("id", "{}.{}".format(func.__module__, func.__name__))
            scheduler.add_job(func, 'interval', seconds=5, args=a, kwargs=k)
        return inner
    return wrapper

@register_job(scheduler, 'date', run_date=datetime.now())
def test2(username):
    print(username)
