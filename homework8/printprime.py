'''
3  多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。

'''
from multiprocessing import Manager,Pool
import time,os
def prime(n):
    print('当前进程号：',os.getpid())
    if (n==1 or n==0):
        return False
    for i in range(2,n+1):
        if(i!=n and n%i==0):
            return False
    return True

def normal():
    time1=time.time()
    num=0
    for j in range(1,100001):
        if(prime(j)):
            num+=1
    time2=time.time()
    print('素数有{0}个,用时{1}'.format(num,time2-time1))

def multy(n):
    time1=time.time()
    po=Pool(n)
    num=0
    for j in range(1,100001):
        n1=po.apply_async(prime,(j,))
        if(n1.get()):
            num+=1
    time2=time.time()
    print('素数有{0}个,{1}个进程用时{2}'.format(num,n,time2-time1))




if __name__=='__main__':
    normal()
    multy(4)
    multy(10)
   





    
    