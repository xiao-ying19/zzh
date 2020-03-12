'''
编写一个函数,接收n个数字，求这些参数数字的和
'''
def sum(*args):
    a=0
    for i in args:
        a+=i
    return a
a=sum(1,2,3,4,5,6,7)
print("和为：",a)