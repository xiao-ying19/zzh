'''
将控制台输入的字符串，转换成元组，并输出显示
'''
x=input("请输入字符串：")
xList=tuple(x.split(","))
xList=[int(xList[i])for i in range (len(xList))]
print(tuple(xList))