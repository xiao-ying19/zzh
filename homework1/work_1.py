"""
输出0-50中的奇数 偶数 质数，能被2和3整除的数
"""
import math
a=[]
b=[]
c=[]
d=[]
for i in range (51):
    if(i%2!=0):
        a.append(i)
    if(i%2==0):
        b.append(i)
    if(i>1):
        for j in range(2,int(math.sqrt(i))+1):
            if(i%j==0 or i==1):
                break                        
        else:
            c.append(i)       
    if(i%2==0 and i%3==0):
        d.append(i)
print('奇数:{0}\n偶数:{1}\n质数:{2}\n能被2和3整除的数:{3}'.format(a,b,c,d))