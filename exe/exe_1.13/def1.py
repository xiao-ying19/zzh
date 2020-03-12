'''
定义一个函数，计算苹果的价格（重量*价格），键盘输入重量和价格
'''
def apple(weigth,price):
    return weigth*price

if __name__=="__main__":
    w=int(input("请输入重量："))
    p=int(input("请输入价格："))
    money=apple(w,p)
    print("总价格是：",money)