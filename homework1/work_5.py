"""
随机生成一个含有20个元素的列表和元组,每个元素在1-100之间
"""
import random
List=[]
Tuple=()
for i in range(20):
    List.append(random.randint(1,100))
    Tuple=Tuple+(random.randint(1,100),)
print("列表：{0}\n元组：{1}".format(List,Tuple))
