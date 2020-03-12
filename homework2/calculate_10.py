'''
编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
'''
def calculate(a,b):
    print("a+b：{0}\na-b:{1}\na*b:{2}".format(a+b,a-b,a*b))
    if not(b==0):
        print("a/b:",a/b)
    else:
        print("除数不能为0")

if __name__=='__main__':
    a=float(input("请输入a:"))
    b=float(input("请输入b:"))
    calculate(a,b)