'''
写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者
'''
def judge_lenth(a):
    return len(a)

if __name__=='__main__':
    obj=eval(input("请输入字符串，列表或元组（字符串请加上引号 ）："))
    print("长度为：",judge_lenth(obj))