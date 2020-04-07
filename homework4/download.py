'''
从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）
'''
import os
import requests
url="https://p5.ssl.qhimgs1.com/sdr/400__/t0102f7dee54b2f2155.jpg"
p="E:/360Downloads"
path=p+url.split("/")[-1]
r=requests.get(url)
r.raise_for_status()
with open(path,'wb')as f:
    f.write(r.content)
print("图片保存成功")
