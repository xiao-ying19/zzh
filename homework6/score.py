'''
六  用面向对象,实现一个学生Python成绩管理系统;
      学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
      实现对学生信息及成绩的增,删,改,查方法;
'''
import os
class StudentScore(object):
      def __init__(self,cl='',id='',name='',pyscore=0):
            self.__class=cl
            self.__id=id
            self.__name=name
            self.__pyscore=pyscore
      def add(self):
            with open('pythonscore.txt','a')as f:
                  f.write(self.__class+'\t'+self.__id+'\t'+self.__name+'\t'+str(self.__pyscore)+'\n')
      def delete(self,key):
            try:
                  data=[]
                  with open('pythonscore.txt')as f:
                        for line in f.readlines():
                              if(line.split('\t')[1]==key):
                                    continue
                              else:
                                    data.append(line)
                  with open('pythonscore.txt','w+')as f:
                        for i in data:
                              f.write(i)


            except FileNotFoundError:
                  print('文件不存在')
      def isexist(self,key):
            with open('pythonscore.txt')as f:
                  for line in f.readlines():
                        if(line.split('\t')[1]==key):
                              return True
            return False
      
      def update(self,key):
            if(self.isexist(key)):
                  self.delete(key)
                  self.add()
      
      def display(self,key):
            with open('pythonscore.txt')as f:
                  for line in f.readlines():
                        a=line.split('\t')
                        if(a[1]==key):
                              print("班级：{0} 学号：{1} 姓名：{2} 成绩：{3}".format(a[0],a[1],a[2],a[3]))
def displayall():
      with open('pythonscore.txt')as f:
            for line in f.readlines()[1:]:
                  i=line.split('\t')[1]
                  StudentScore().display(i)



if __name__=='__main__':
      print("————————欢迎来到学生成绩管理系统————————")
      while(True):
            print("1:增加学生成绩信息\n2:删除学生成绩信息\n3:修改学生成绩信息\n4:查找学生成绩信息\n5:打印全部成绩信息\n0:退出\n")
            n=int(input("请输入："))
            if(n==1):
                  cl=input("输入班级：")
                  id=input("输入学号：")
                  name=input("输入姓名：")
                  score=input("输入成绩：")
                  s=StudentScore(cl,id,name,score)
                  s.add()
                  print("插入成功")
                  
            elif(n==2):
                  s=StudentScore()
                  id=input("请输入要删除信息的学号：")
                  if(s.isexist(id)):
                        s.delete(id)
                        print("删除成功")
                  else:
                        print("学生不存在")
                  
            elif(n==3):
                  s=StudentScore()
                  id=input("请输入要修改信息的学号：")
                  if(s.isexist(id)):
                        s.delete(id)
                        cl=input("请输入改后的班级：")
                        ID=input("请输入改后的学号：")
                        name=input("请输入改后的姓名：")
                        score=input("请输入改后的成绩：")
                        s.__init__(cl,ID,name,score)
                        s.add()
                        print("修改成功")
                  else:
                        print("信息不存在")
                  
            elif(n==4):
                  s=StudentScore()
                  id=input("请输入要查找的学号：")
                  if(s.isexist(id)):
                        s.display(id)
                  else:
                        print("信息不存在")
            elif(n==5):
                  displayall()
                  
            else:

                  break



