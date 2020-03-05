"""
设计一个猜数字游戏：最多只能猜N次，在N次之内猜不出就退出程序，提示猜测失败
系统随机生成一个1-100的整数
用户猜数字，系统给出相应的提示
最多只能猜6次，大于6次，游戏结束
"""
import random
number=random.randint(1,100)
chances=6
print("="*40)
print('游戏开始！')
while(chances>0):
    print("="*40)
    a=int(input("请输入数字,您有{}次机会：".format(chances)))
    if(a>number):
        print("输入的大了，再小一点吧~")
        chances-=1
        continue
    elif(a<number):
        print("输入的小了，再大一点吧~")
        chances-=1
        continue
    elif(a==number):
        chances-=1
        print("游戏成功！共用{}次".format(6-chances))
        break
if(chances<=0):
    print("游戏失败，请重新开始！")


    




