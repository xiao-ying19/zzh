'''
3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
'''
import os
List=[]
try:
    with open("stu.txt") as f:
        lines=f.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
        List.append(line.strip().split('\t'))
    a=sorted(List[1:-1],key=lambda student: int(student[2]))
    for i in a:
        print(' '.join(i))
   
   
            
        


    