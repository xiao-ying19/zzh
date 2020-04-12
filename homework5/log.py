'''
2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
'''
def log(func):
    def inner(*args,**kwargs):
        with open('log.txt','a') as f:
            f.write(func.__name__+"\n")
        func()
    return inner()
@log
def func_1():
    print("fun_1执行一次")
@log
def func_2():
    print("func_2执行一次")

func_1()

