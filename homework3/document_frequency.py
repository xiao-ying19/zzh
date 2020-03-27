'''
  在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 
  请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
    比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
'''
import os
import re
import json
#统计一篇文章的词频 并写入文件
def frequency(article):
    Dict={}
    for i in re.finditer(r'[a-zA-Z]+',article):
        if(i.group(0) in Dict.keys()):
            Dict[i.group(0)]+=1
        else:
            Dict[i.group(0)]=1
    with open("result.txt","a+")as f:
        json.dump(Dict,f)
        f.write("\n\n")
    return Dict
    #比较相似度
def compare(Dict1,Dict2):
    num=0
    Dict1=sorted(Dict1.items(),key=lambda item:item[1],reverse=True)[0:10]
    Dict2=sorted(Dict2.items(), key=lambda item:item[1],reverse=True)[0:10]
    for item in Dict1:
        if(Dict2.count(item)>0):
            num+=1
    return num/10

if __name__=='__main__':
    try:
        with open("article1.txt") as f1:
            a=f1.read()
        with open("article2.txt")as f2:
            b=f2.read()
    except FileNotFoundError:
        pass
    else:
        Dict1=frequency(a)
        Dict2=frequency(b)
        result=compare(Dict1,Dict2)
        print("相似度为{:.2f}%".format(result*100))



    
