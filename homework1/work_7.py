"""
打印输出9*9乘法表 ，注意格式
"""
for i in range(1,10):
    for j in range(1,i+1):
        print("{0}×{1}={2}".format(j,i,i*j),end=" ")
    print("\n")
