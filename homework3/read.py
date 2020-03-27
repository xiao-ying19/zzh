'''
2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx
'''
import os
import sys
a=[]
try:
    with open("input.txt")as f:
        for num,value in enumerate(f):
            b=[value.strip()]
            a.append(b)
            print("第{0}行：{1}".format(num+1,value))
except FileNotFoundError:
    pass


