'''
4 多进程通讯：
  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；
'''
from multiprocessing import Process,Queue
import random,time

def write(q,a):
  
  q.put(a)
  time.sleep(random.random())

def read(q):
  while(True):
    value=q.get(True)
    print('get %s from queue.'%value)

if __name__=='__main__':
  q=Queue()
  a=input('请输入：')
  pw=Process(target=write,args=(q,a))
  pr=Process(target=read,args=(q,))
  pw.start()
  pr.start()
  pw.join()
  pr.terminate()
  
