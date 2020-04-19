'''
五  请写一个小游戏，人狗大站;  规则:
    1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
        人的打击力为30;  初始化血为100;    狗的攻击力为 35; 初始化血为80;
    2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
        人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
    3   对战规则: 
     A  随机决定,谁先开始攻击; 
     B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
     C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件；
 在写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）
'''
import random
from dogsTeam import DogsClass
from peopleTeam import PeopleClass

def display(dogs,people):
    for i in range(len(dogs)):
        print(str(dogs[i].num)+"号狗：血量"+str(dogs[i].blood)+"攻击力"+str(dogs[i].power))
    for j in range(len(people)):
        print(str(people[j].num)+"号人：血量"+str(people[j].blood)+"攻击力"+str(people[j].power))



if __name__=='__main__':
    print("--"*50)
    print("游戏开始")
    dogs=[DogsClass() for i in range(3)]
    people=[PeopleClass() for i in range(2)]
    display(dogs,people)
    order=random.choice([0,1])#随机决定顺序，0代表狗先攻击
    round=1
    while(len(dogs)>0 and len(people)>0):
        #round=1 #轮次
        print("--"*50+"\n第"+str(round)+"轮")
        if(order==0):#
            print("狗攻击人")
            #优先选择攻击力最高的狗
            dogs.sort(key=lambda x:x.power,reverse=True)
            a_dog=dogs[0]
            #随机选择一个人
            n=random.randint(0,len(people)-1)
            a_people=people[n]
            a_people.attacked(a_dog)
            if(a_people.blood<=0):
                people.pop(n)
            order=1
        else:#人攻击狗
            print("人攻击狗")
            #优先选择攻击力最高的人
            people.sort(key=lambda x:x.power,reverse=True)
            a_people=people[0]
            n=random.randint(0,len(dogs)-1)
            a_dog=dogs[n]
            a_dog.attacked(a_people)
            if(a_dog.blood<=0):
                dogs.pop(n)
            order=0
        display(dogs,people)
        round+=1
    if(len(dogs)<=0):
        print("人获胜！")
    else:
        print("狗获胜！")




