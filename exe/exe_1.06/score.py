'''
用列表定义10个同学的成绩，输出最高分，最低分，总分和平均值
'''
score=[89,78,67,77,65,95,45,67,43,67]
sum=0
for i in score:
    sum=sum+i
print("最高分：{0}\n最低分：{1}\n总分：{2}\n平均值：{3}".format(max(score),min(score),sum,sum/10))
