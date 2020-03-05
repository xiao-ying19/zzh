"""
前面两个元素为0，1  输出100以内的斐波那契数列
"""
List=[0,1]
n=0
index=2
while(n<=100):
    n=List[index-1]+List[index-2]
    if(n<100):
        List.append(n)
    index+=1
print("100以内的斐波那契数列为：",List)