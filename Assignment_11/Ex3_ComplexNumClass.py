class ComplexNum:

    def __init__(self,r,i):
        self.real=r
        self.imagin=i

    def show(self):
        print(self.real,"+",self.imagin,"i")

    def Sum(self,other):
        r_new=self.real+other.real
        i_new=self.imagin+other.imagin
        x=ComplexNum(r_new,i_new)
        return x

    def Sub(self,other):
        r_new=self.real-other.real
        i_new=self.imagin-other.imagin
        x=ComplexNum(r_new,i_new)
        return x

    def Mult(self,other):
        r_new=self.real*other.real-self.imagin*other.imagin
        i_new=self.real-other.imagin+self.imagin*other.real
        x=ComplexNum(r_new,i_new)
        return x

    
#Use example
a=ComplexNum(3,4)
a.show()
   
b=ComplexNum(6,9)
b.show()

c=a.Sum(b)
c.show()

c=a.Sub(b)
c.show()

c=a.Mult(b)
c.show()