'''
定义一个字符串，分别进行查找某个字符串是否包含在这个字符串里面；进行某个字符串的替换，打印字符串的长度
'''
string='You are a good student!'
print("长度是：",len(string))       #打印长度
if(string.find('student')!=-1):     #查找
    print(True)
new_string=string.replace('good','bad')        #替换
print("替换之后的字符串：",new_string)