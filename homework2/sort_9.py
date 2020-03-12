'''
定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
'''
def list_sort(List):
    return sorted(List)
if __name__=='__main__':
    List=[10,9,8,7,6,5,4,3,2,1]
    print(list_sort(List))
