'''
京东二面笔试题
1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
'''
import os
import random

ip=['172.25.254.'+str(i) for i in range(1,255)]

# with open("ip.txt","w")as f:
#     for count in range(1200):
#         a=random.sample(ip,1)[0]
#         f.write(a+"\n")
Dict={}
try:
    f=open("ip.txt")
except FileNotFoundError:
    print("文件不存在")
else:
    for line in f.readlines():
        if(line in Dict.keys()):
            Dict[line]+=1
        else:
            Dict[line]=1
    new_List=sorted(Dict.items(),key=lambda x:x[1],reverse=True)[:10]
    for i in new_List:
        print(i[0].strip(),i[1])

    

        
