'''
写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
'''
def dist_cut(a_dist):
    for key,value in a_dist.items():
        if len(value)>2:
            a_dist[key]=value[0:2]
    return a_dist
if __name__=='__main__':
    example={'组长':'张三','学号':'123456','小组成员':['王五','李明','张小明']}
    print("新的字典：",dist_cut(example))