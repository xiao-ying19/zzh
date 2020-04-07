'''
定义一个函数，判断一个输入的日期，是当年的第几周，周几？ 
 将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
'''
from datetime import datetime
#from datetime import timedelta
def Calendar(str):
    cday=datetime.strptime(str,'%Y-%m-%d')
    week=datetime.date(cday).isocalendar()
    return cday,week

if __name__=='__main__':
    str="2020-8-20"
    cday,week=Calendar(str)
    print("{0}是当年的第{1}周周{2}".format(str,week[1],week[2]))
    date1=Calendar('2020-8-23')[0]
    date2=Calendar('2020-2-17')[0]
    if(cday>date1 or cday <date2):
        print("华电校历：寒假")
    else:
        school=int((cday-date2).days/7)+1
        print("华电校历：第{}周".format(school))


    


