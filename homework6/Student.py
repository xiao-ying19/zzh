'''
四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
      封装方法，求单个学生的总分，平均分，以及打印学生的信息。
'''
class Stu(object):
    def __init__(self,name,age,sex,es,ms,cs):
        self.__name=name
        self.__age=age
        self.__sex=sex
        self.__es=es
        self.__ms=ms
        self.__cs=cs

    def sum(self):
        return self.__es+self.__ms+self.__cs
    def average(self):
        return self.sum()/3
    def toString(self):
        print("姓名:{}".format(self.__name))
        print("年龄:{}".format(self.__age))
        print("性别:{}".format(self.__sex))
        print("英语:{}".format(self.__es))
        print("数学:{}".format(self.__ms))
        print("语文:{}".format(self.__cs))
        print("总成绩:{}".format(self.sum()))
        print("平均：{}".format(self.average()))
s1=Stu('张三',19,'男',99,66,78)
s1.toString()

