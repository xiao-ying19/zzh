'''
 通过Python来模拟实现一个txt文件的拷贝过程;
'''
import os
def copy(path1,path2):
    try:
        f1=open(path1)
        f2=open(path2,"w")
    except FileNotFoundError:
        print("找不到文件！")
    else:
        for f in f1:
            f2.write(f)
        f1.close()
        f2.close()

copy("file1.txt","file2.txt")
        
