'''
文件综合迷你编程项目
'''
import os
para='''
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind

'''
#创建文件
with open("Blowing in the wind.txt","w")as f:
    f.write(para)
#插入
try:
    with open ("Blowing in the wind.txt") as f:
        lines=f.readlines()
except:
    pass
else:
        a=[line.strip()for line in lines]
        a.insert(0,'Blowing in the wind')
        a.insert(1,'Bob Dylan')
        a.insert(-1,"1962 by Warner Bros.Inc.")
with open ("Blowing in the wind.txt","w")as f:
    for i in a:
        f.write(' '.join(i)+'\n')
with open("Blowing in the wind.txt")as f:
    print(f.read())
        

