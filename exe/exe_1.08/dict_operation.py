'''
字典元素的增加，修改，删除；并观察输出
'''
Dict={'name':'Tom','age':'19','school':'ncepu'}
Dict['class']='First'       #增加
Dict['age']='20'        #修改
del Dict['school']      #删除
for key,value in Dict.items():      #输出
    print("{0}:{1}".format(key,value))
