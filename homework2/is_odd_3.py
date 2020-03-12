'''
编写一个函数, 传入一个数字列表, 输出列表中的奇数;
数字列表请用随机数函数生成;
'''
import random
def is_odd(List):
    final_List=[]
    for i in List:
        if(i%2==1):
            final_List.append(i)
    return final_List

if __name__=='__main__':
    List=[]
    for i in range (10):
        List.append(random.randint(0,20))
    print("原列表：{0}\n奇数列表：{1}".format(List,is_odd(List)))