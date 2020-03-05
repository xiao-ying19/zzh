"""
筛选字典中元素
"""
student={'120':81,'121':75,'122':86,'123':97,'124':22,'125':67,'126':45,'127':68,'128':86,'129':44,'130':63}
print("所有学生成绩为：{}\n80分以上的有：".format(student))
for key,value in student.items():
    if(value>=80):
        print('{0}:{1}'.format(key,value))