'''
 请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
 例如，输入 aaaabbc，输出：a:4
'''
def max_times(string):
    a_dict={}
    for s in string:
        if (s in a_dict.keys() ):
            a_dict[s]+=1
        else:
            a_dict[s]=1
    for key,value in a_dict.items():
        if(value==max(a_dict.values())):
            print("{0}:{1}".format(key,value))

if __name__=='__main__':
    Str='aaaa444'
    max_times(Str)