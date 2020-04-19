class DogsClass(object):
    num=1
    def __init__(self):
        self.num=DogsClass.num
        self.blood=80
        self.power=35
        DogsClass.num+=1
    def attacked(self,people):
        self.blood-=people.power
        self.power-=3


