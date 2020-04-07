'''
通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
    名称         日期                   类型（文件夹或者 文件）       大小
'''
import os
import time
def isfile(path):
    if(os.path.isfile(path)):
        return "文件"
    else:
        return "文件夹"

path="D:/git_workspace"
dir=os.listdir(path)
List=[['名称','日期','类型（文件夹或者文件）','大小']]
for file in dir:
    a=[]
    newpath=os.path.join(path,file)
    a.append(file)
    a.append(time.ctime(os.path.getctime(newpath)))
    a.append(isfile(newpath))
    a.append(os.path.getsize(newpath))
    List.append(a)
#print(List)
tplt="{0:{4}^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:^10}"
for l in List:
    print(tplt.format(l[0],l[1],l[2],l[3],chr(12288)))


    


