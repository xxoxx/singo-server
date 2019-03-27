def decorator(f):
    def inner(*args,**kwargs):
        print('start inner')
        print(*args)
        print(**kwargs)
        f(*args,**kwargs)
        print('end inner')
    print(decorator.__name__)
    return inner

@decorator
def foo(*args,**kwargs):
    print(sum(args))
    print('foo')


foo(2, 3, 4)