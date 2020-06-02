"""
4 爬取这个网址上https://www.programcreek.com/python/，搜索requests的范例代码；保存到txt文件中（只保留文字）；
"""


import requests
import re
from bs4 import BeautifulSoup
import os


def geturl(url,headers):#  获取所有模块的链接
    try:
        res =requests.get(url,headers=headers)
        url_list=re.findall(r'https:\/\/www.programcreek.com\/python\/example\/[0-9]+\/requests\.[a-zA-Z_0-9]*',res.text)
    except Exception as e:
        print(e)
    return url_list


def spider(one_url,headers):#  获取练习题
    try:
        res =requests.get(one_url,headers=headers).content.decode('utf-8')
        soup =BeautifulSoup(res,'html.parser')
        s =soup.find_all('pre')
        with open('exe.txt','a+')as f:
            for i in range(len(s)):
                if s[i].string ==None:
                    pass
                else:
                    f.write(s[i].string)
                    f.write('\n\n')
    except Exception as e:
        print(e)
    return s


if  __name__ =='__main__':
    url='https://www.programcreek.com/python/index/221/requests'
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    list =geturl(url,headers)
    spider(list[1],headers)
    # for i in list:
    #     spider(i)


