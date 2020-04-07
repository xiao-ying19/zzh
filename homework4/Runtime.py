'''
定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
    提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
'''
from collections import deque
import time
def time1(List):
    a=time.time()
    List.insert(0,-1)
    List.append(11)
    print(List)
    b=time.time()
    return b-a
def time2(List):
    a=time.time()
    List.appendleft(-1)
    List.append(11)
    print(List)
    b=time.time()
    return b-a
if __name__=='__main__':
    List1=[i for i in range(10)]
    List2=deque(List1)
    time1=time1(List1)
    time2=time2(List2)
    print("自带函数所用时间：{}\ndeque模块所用时间：{}\n时间差：{}".format(time1,time2,time1-time2))

