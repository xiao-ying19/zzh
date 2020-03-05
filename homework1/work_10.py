'''
统计一篇文章中每个单词出现的次数，打印输出，按照词频从高到低输出
'''
import re
str="""
With the development of living standards,
 going out to have a tourism is becoming a part of our life. 
 But at the same time, uncivilized behaviors in tourism are frequently happening. 
 So cultural tourism has became a hot topic in the society.
"""
dist={}
pat='[a-zA-Z]+'
List=re.findall(pat,str)
for word in List:
    if not(word in dist.keys()):
        dist[word]=1
    else:
        dist[word]+=1
d_order=sorted(dist.items(),key=lambda x: x[1],reverse=True)
print(d_order)
