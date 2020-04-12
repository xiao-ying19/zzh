'''
 编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
     三个目标函数分别为：
     A 打印输出20000之内的素数；
     B 计算整数2-10000之间的素数的个数；
     C 计算整数2-M之间的素数的个数；
  可以观看给的视频材料，仿照示例来做；
'''
def A1(func):
    def inner():
        func()
    return inner()

def B2(func):
    def inner():
        res=func()
        return res
    return inner


# @A1
# def A():  
#     #打印输出20000之内的素数（无参无返回值）
#     n=2
#     while(n<=100):
#         flag=0
#         k=2
#         while(k<n):
#             if(n%k==0):
#                 flag=1
#                 break
#             else:
#                 k+=1
        
#         if(flag==0):
#             print(n)
#         n+=1
@B2      
def B():
    #计算整数2-10000之间的素数的个数；(有返回值)
    n=2
    num=0
    while(n<=100):
        flag=0
        k=2
        while(k<n):
            if(n%k==0):
                flag=1
                break
            else:
                k+=1
        
        if(flag==0):
            num+=1
        n+=1
    return num
print('2-10000之间的素数个数：%s'%(B()))

def C(M):
    #计算整数2-M之间的素数的个数；(有参数)
    n=2
    while(n<=100):
        flag=0
        k=2
        while(k<n):
            if(n%k==0):
                flag=1
                break
            else:
                k+=1
        
        if(flag==0):
            print(n)
        n+=1
    