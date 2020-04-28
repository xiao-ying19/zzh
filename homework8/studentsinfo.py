'''
 有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；
'''
from multiprocessing.pool import ThreadPool
import time
import random

def task(*args):
    for a_data in args:
        print(a_data)


if __name__=='__main__':
    score=[random.randint(0,100) for i in range(100)]
    pool=ThreadPool(5)
    pool.apply_async(task,args=score[:20])
    pool.apply_async(task,args=score[20:40])
    pool.apply_async(task,args=score[40:60])
    pool.apply_async(task,args=score[60:80])
    pool.apply_async(task,args=score[80:])
    pool.close()
    pool.join()
    print('completed')

