'''
三、定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
 '''
class dictclass(object):
    def __init__(self,a_dict):
        self.a_dict=a_dict
    def del_dict(self,key):
        self.a_dict.pop(key)
        return self.a_dict
    def get_dict(self,key):
        if(key in self.a_dict.keys()):
            return self.a_dict[key]
        else:
            return 'not found'
    def update_dict(self,otherDict):
        newDict=dict(self.a_dict.items()+otherDict.items())
        return list(newDict.values())

    def get_key(self):
        return list(self.a_dict.keys())
d=dictclass({'1':'a','2':'aa'})
#print(d.del_dict('1'))
#print(d.get_dict('1'))
print(d.get_key())
    
    


    
# dic={'1':1,'2':2}
# print(list(dic.keys()))