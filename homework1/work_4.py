"""
判断用户输入的年份是否为闰年
"""
year=int(input("请输入年份"))  #注意数据类型转换
if(year%100==0): 
    if(year%400==0):
        print(year, " is 世纪闰年")
    else:
        print(year,"不是闰年")
elif(year%4==0):   
        print(year ,"is 普通闰年")       
else:
    print(year ,"不是闰年")

