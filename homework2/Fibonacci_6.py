'''
定义一个函数, 打印输出n以内的斐波那契数列
'''
def Febonacci(n):
    a=[1,1]
    flag=2
    next_num=a[flag-1]+a[flag-2]
    while(next_num<=n):
        a.append(next_num)
        flag+=1
        next_num=a[flag-1]+a[flag-2]
    return a

if __name__=='__main__':
    n=100
    print(Febonacci(n))
