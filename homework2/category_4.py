'''
写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
'''
def str_category(str):
    num=[]
    word=[]
    space=[]
    others=[]
    for s in str:
        if(s>='a'and s<='z' or s>='A' and s<='Z'):
            word.append(s)
        elif(s>='0 'and s<='9'):
            num.append(s)
        elif(s==' '):
            space.append(s)
        else:
            others.append(s)
    return word,num,space,others

if __name__=='__main__':
    str=input("请输入字符串：")
    List=str_category(str)
    print("字母：{0}个\n数字：{1}个\n空格：{2}个\n其他字符：{3}个".format(len(List[0]),len(List[1]),len(List[2]),len(List[3])))