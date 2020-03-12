'''
创建一个有10个数字的列表，先输出此列表，然后输出其中的偶数元素
'''
import random
List=[random.randint(1,50) for i in range(20)]
print(List)

for i in List:
    if(i%2==0):
        print(i,end=' ')