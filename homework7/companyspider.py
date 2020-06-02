"""
2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库
"""

from bs4 import BeautifulSoup
import re
import requests


def geturl():
    try:
        with open('Url.txt') as f:
            List=[i for i in f.readlines()]
    except Exception as e:
        print(e)
    return List


def spider(a_url,headers):
    try:
        res =requests.get(a_url,headers=headers).content.decode('utf-8')
        print(res)
        soup =BeautifulSoup(res,'html.parser')
        introduce=soup.find_all('a',text=re.compile(r'关于我们|企业介绍|企业发展|历史|概况'))
        print(introduce)
        for a in introduce:
            u=a.attrs['href']
    except Exception as e:
        print(e)
    print(u)





if __name__=='__main__':
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    List =geturl()
    spider(List[0],headers)
    for a_url in List:
        spider(a_url,headers)





