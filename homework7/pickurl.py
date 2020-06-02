"""
1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
   提示，文件有1000行，注意控制每次读取的行数；
"""
import re
import os
if __name__=='__main__':
    with open('webspiderUrl.txt',encoding='utf-8') as fr:
        with open('Url.txt','a')as fw:
            for line in fr.readlines():
                res=re.search(r'(http|ftp|https):\/\/[\s\w\-_]+(\.[\s\w\-_]+)+([\s\w\-\.,@?^=%&:/~\+#]*[\s\w\-\@?^=%&/~\+#])?',line)
                if res:
                    fw.write(res.group()+'\n')
                else:
                    print('{}未提取出Url'.format(line))
            
    



    