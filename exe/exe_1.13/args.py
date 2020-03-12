'''
使用不定长参数定义一个函数，实现对输入数据的封装（封装成一个列表和字典），然后打印输出
'''
def myfun(*args):
    List=[i for i in args]
    print(List)
myfun(22,33,'a',77)