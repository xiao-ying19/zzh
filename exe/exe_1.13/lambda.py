'''
初始化一个列表（1~20之间的整数）；然后，使用匿名函数，列表解析式，来打印输出一个列表中的奇数
'''
List=[i for i in range(1,21)]
print(List)
odd=list(filter(lambda x:x%2==1,List))
print(odd)