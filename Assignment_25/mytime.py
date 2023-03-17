
class MyTime():
    def __init__(self,h,m,s):
        self.hour=h
        self.min=m
        self.sec=s
    
    def plus(self):
        self.sec+=1
        if self.sec>=60:
            self.min+=1
            self.sec-=60
        if self.min>=60:
            self.hour+=1
            self.min-=60

    def minus(self):
        self.sec-=1
        if self.sec<0:
            self.min-=1
            self.sec=59
        if self.min<0:
            self.hour-=1
            self.min=59
