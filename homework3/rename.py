'''
4 题目要求：
 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
 将当前img目录所有以.png结尾的后缀名改为.jpg.
'''
import os
import random
import string
def create_file():
    try:
        os.mkdir("img")
    except:
        print("文件已存在")
#生成10个文件
    else:
        for i in range(10):
            name=random.sample(string.ascii_letters+string.digits,4)
            name=' '.join(name)
            fp= open('img/'+name+'.png','w')
            fp.close()

#找出以.png结尾的文件
pngfind=[filename for filename in os.listdir("img") if filename.endswith(".png")]
basefile=[os.path.splitext(filename)[0] for filename in pngfind]
for filename in basefile:
    oldname=os.path.join("img",filename+".png")
    newname=os.path.join("img",filename+".jpg")
    os.rename(oldname,newname)
        