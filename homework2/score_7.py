'''
随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
    A---成绩>=90;  
    B-->成绩在 [80,90)
    C-->成绩在 [70,80)
    D-->成绩<70
'''
import random
def judge_level():
    score=[random.randint(0,100) for i in range (20)]
    level=[]
    for a_score in score:
        if(a_score>=90):
            level.append('A')
        elif(a_score>=80 and a_score<90):
            level.append('B')
        elif(a_score>=70 and a_score<80):
            level.append('C')
        else:
            level.append('D')
    return score,level

if __name__=='__main__':
    List=judge_level()
    print("成绩:{0}\n等级：{1}".format(List[0],List[1]))

