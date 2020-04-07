'''
从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
        Tom   admin   XXXXX
        Jack   root      XXXXX   
'''
import os
import hashlib

students=[]
sha1=hashlib.sha1()
for i in range(5):
    a=input("输入姓名，账号和密码（用空格隔开）").split(" ")
    sha1.update(a[2].encode('utf-8'))
    a[2]=sha1.hexdigest()
    students.append(a)

str=""
for stu in students:
        for i in range (len(stu)):
            str=str+stu[i]+'\t'
        str=str+"\n"
with open("stu.txt","w") as f:
    f.write(str)
    
    
    


    