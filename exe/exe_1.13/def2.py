'''
定义一个函数，打印输出列表里的元素，然后增加列表中的元素，然后再输出新的列表；主程序中，打印这个列表的地址（传参之前，之后)

'''
def printList(List):
    List.append(1)
    print(List)
    List.append('b')
    print(List)

if __name__=='__main__':
    List=[]
    print("传参之前：",id(List))
    printList(List)
    print("传参之后：",id(List))
