'''
定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
       实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
'''
import random
class dog(object):
    dogs=[{'color':'black','num':10,'price':200},{'color':'gray','num':9,'price':150},{'color':'white','num':11,'price':200}]
    def buy(self):
        for a_dog in self.dogs:
            a_dog['num']+=5 #每种狗买进5只
           
    def sell(self):
        i=random.randint(0,2)
        self.dogs[i]['num']-=1
a=dog()
a.buy()
a.sell()
a.sell()
for a_dog in a.dogs:
    print('color:{0}  num:{1}'.format(a_dog['color'],a_dog['num']))


