'''
1  编写一个装饰器，能计算其他函数的运行时间；
'''
import time
def timmer(fun):
    def inner():
        startTime=time.time()
        fun()
        endTime=time.time()
        print("函数执行的时间为：%s"%(endTime-startTime))
    return inner()

@timmer
def fun():
    time.sleep(5)

# if __name__=='__main__':
#     fun()