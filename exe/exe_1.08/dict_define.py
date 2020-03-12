'''
定义一个字典，存放某个同学的信息（学号，姓名，班级，年龄）；再定义另外一个字典，存放5个同学的学号，姓名信息
通过键来访问相应的数据，或者整体输出
'''
dict_1={"name":"Tom","ID":"123456","class":"one","age":20}
dict_2={"Alice":"123","Tom":"124","John":"135","Tedy":"154","Hone":"178"}
for key,value in dict_1.items():
    print("{0}:{1}".format(key,value))
print(dict_2["Alice"])