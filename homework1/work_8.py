"""
设计一个数据结构，存放10个员工的信息并初始化，每个员工的信息包括：工号，姓名，工龄，工资；按照工资从高到低打印输出
"""

workers=[{'工号':'10','姓名':'张三','工龄':10,'工资':12000},
{'工号':'11','姓名':'李四','工龄':20,'工资':22000},
{'工号':'12','姓名':'塞班','工龄':11,'工资':12500},
{'工号':'13','姓名':'郑长海','工龄':15,'工资':10500},
{'工号':'14','姓名':'王五','工龄':16,'工资':8000},
{'工号':'15','姓名':'刘晓明','工龄':26,'工资':9000},
{'工号':'16','姓名':'张旭','工龄':6,'工资':10000},
{'工号':'17','姓名':'李丽','工龄':9,'工资':18000},
{'工号':'18','姓名':'刘强','工龄':19,'工资':28000},
{'工号':'19','姓名':'徐凯','工龄':22,'工资':38000}]
salarys=[]
for worker in workers:
    salarys.append(worker['工资'])
print("10名员工的信息如下（按工资由高到低排序）：")
while(len(salarys)>=1):
    index=salarys.index(max(salarys))
    print(workers[index])
    salarys.pop(index)
    workers.pop(index)

