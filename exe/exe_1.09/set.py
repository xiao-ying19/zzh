'''
定义一个集合类型的变量（用两种方法初始化）然后进行相应的元素的操作
'''
a={1,2,3,4,5}
b=set([1,2,3,4,5])
c=a.copy()#拷贝
a.add(10) #添加
a.update(['小明'])
a.remove(1) #移除
b.clear()#清空
d=a.intersection(c)
print("集合a:{0}\n集合c：{1}\n集合a与c的交集：{2}".format(a,c,d))


