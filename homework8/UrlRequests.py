'''
 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；
提示 ：使用requests模块
'''
import requests
import threading
import queue
import os

def getLinkList():
    List=[]
    try:
        with open('url_data.txt') as f:
            for line in f.readlines():
                List.append(line)
    except FileNotFoundError:
        print('文件找不到')
    
    return List


class myThread(threading.Thread):
    def __init__(self,name,q):
        threading.Thread.__init__(self)
        self.name=name
        self.q=q
        
    def run(self):
        crawler(self.name,self.q)
        
def crawler(threadName,q):
    url=q.get(timeout=2)
    try:       
        r = requests.get(url,timeout=30)    
        r.raise_for_status()       
        r.encoding = r.apparent_encoding
        return r.text
    except:
         print('{}不可访问'.format(url))

if __name__=='__main__':
    threadList=['Thread-1','Thread-2','Thread-3','Thread-4','Thread-5']
    q=queue.Queue(1000)
    threads=[]
    for T_name in threadList:
        thread=myThread(T_name,q)
        thread.start()
        threads.append(thread)

    for url in getLinkList():
        q.put(url.strip())
    
    for i in threads:
        i.join()
