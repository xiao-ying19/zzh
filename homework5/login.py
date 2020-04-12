'''
3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
'''
def login(func):
    def inner(*args,**kwargs):
        Dict={}
        with open('user.txt')as f:
            for line in f.readlines():
                Dict[line.split('\t')[0]]=line.split('\t')[1].strip()
        userName=input("请输入账号：")
        if(userName in Dict.keys()):
            passWord=input("请输入密码：")
            if(Dict[userName]==passWord):
                func()
               
            else:
                print("密码不正确")
        else:
            print("信息不存在 ")
    return inner()

@login
def func():
    print("可以调用此函数了")
        



       

        
