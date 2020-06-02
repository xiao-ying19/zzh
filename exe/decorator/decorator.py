"""
定义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志;
"""
def log(func):
    def sum(x,y):
        print('call %s()' % func.__name__)
        res=func(x,y)
        print('sum:%.2f' % res)
    return sum

@log
def sum(x,y):
    return x+y

sum(1,2)