class Time:
    def __init__(self, hour = 0, minute = 0, second = 0):
        # Properties

        if second>=60:
         while second>=60:
            minute+=1
            second-=60
        elif second<0:
            while second<0:
                minute-=1
                second+=60

        if minute>=60:
            while minute>=60:
                hour+=1
                minute-=60
        elif minute<0:
            while minute<0:                
                hour-=1
                minute+=60
                
        self.hour = hour
        self.minute = minute
        self.second = second




    # Methods
    def Show(self):
        print(self.hour,":",self.minute,":",self.second)


    def Sum(self,other):
        s_new=self.second+other.second
        m_new=self.minute+other.minute
        h_new=self.hour+other.hour
        t=Time(h_new,m_new,s_new)
        return t


    def Subtract(self,other):
        s_new=self.second-other.second
        m_new=self.minute-other.minute
        h_new=self.hour-other.hour
        t=Time(h_new,m_new,s_new)
        return t


    # def ConvertSecondToTime(self):
    #     h=0
    #     m=0
    #     s=0
    #     while self.second>=3600:
    #         self.second-=3600
    #         h+=1

    #     while self.second>=60:
    #         self.minute-=60
    #         m+=1

    #     s=self.second

    #     t=Time(h,m,s)
    #     return t



    def ConvertTimeToSecond(self):
        return self.hour*3600+self.minute*60+self.second

    def ConvertGMTtoTehran(self):
        gmt_dif=Time(3,30,0)
        Tehran_Time=self.Sum(gmt_dif)
        return Tehran_Time


#Use example
a=Time(5,6,81)
a.Show()

b=Time(12,61,35)
b.Show()

c=a.Sum(b)
c.Show()

h=a.Subtract(b)
h.Show()

l=Time(5,3,9)
print(l.ConvertTimeToSecond())

s=Time(0,0,6000)
s.Show()

gmt=Time(7,0,0)
gmt.ConvertGMTtoTehran().Show()


