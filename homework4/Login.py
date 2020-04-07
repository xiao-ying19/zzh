'''
(继续上面的练习) 模拟用户登录:
     5个同学的姓名,账号和密码(加密后的),保存在一个文件上;  
      系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）; 
       如果都正确,打印提示, 您登录成功(失败);
'''
import os
import hashlib
flag=0
name=input("请输入同学姓名：")
try:
     with open("stu.txt")as f:
          for line in f.readlines():
               line=line.split("\t")
               if(name==line[0]):
                    flag=1
                    pw=line[2]
                    break        
except FileNotFoundError :
          print("找不到文件")
else:
     if(flag==0):
          print("找不到此人")
     else:
          password=input("请输入密码：")
          sha1=hashlib.sha1()
          sha1.update(password.encode("utf-8"))
          if(sha1.hexdigest()==pw):
               print("登陆成功！")
          else:
               print("登陆失败！")


