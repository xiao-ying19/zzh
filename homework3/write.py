'''
1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
'''
import os
a=[]
print("请输入文字信息：")
while(True):
    b=[]
    str=input()   
    if(len(str)!=0):
        b.append(str)
        a.append(b)
    else:
        break
with open("input.txt","w") as f:
    for i in a:
        f.write(' '.join(i))
        f.write("\n")

        

