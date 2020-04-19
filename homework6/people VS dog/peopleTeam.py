class PeopleClass(object):
    num=1
    def __init__(self):
        self.num=PeopleClass.num
        self.blood=100
        self.power=30
        PeopleClass.num+=1
    def attacked(self,dog):
        self.blood-=dog.power
        self.power-=2
