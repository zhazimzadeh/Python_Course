class Fraction:
    def __init__(self, numerator , denominator ):
        # Properties
        self.numerator = numerator

        if denominator != 0:
            self.denominator = denominator
        else:
            raise ZeroDivisionError
        

    # Methods
    def Show(self):
        print(self.numerator,"/",self.denominator)

    def Sum(self,Frac1,Frac2):
        num=Frac1.numerator*Frac2.denominator+Frac1.denominator*Frac2.numerator
        denom=Frac1.denominator*Frac2.denominator
        x=Fraction(num,denom)
        return x

    def Subtract(self, other):
        num=Frac1.numerator*Frac2.denominator-Frac1.denominator*Frac2.numerator
        denom=Frac1.denominator*Frac2.denominator
        x=Fraction(num,denom)
        return x

    def Multiply(self,Frac1,Frac2):
        num=Frac1.numerator*Frac2.numerator
        denom=Frac1.denominator*Frac2.denominator
        x=Fraction(num,denom)
        return x

    def Divide(self,Frac1,Frac2):
        num=Frac1.numerator*Frac2.denominator
        denom=Frac1.denominator*Frac2.numerator
        x=Fraction(num,denom)
        return x
    
    def ConvertFracToNum(self):        
        return self.numerator/self.denominator

    
    def Simplify(self):

        GCD = 0
        n=max(self.numerator,self.denominator)
        for i in range(1, n + 1):  
            if (( self.numerator % i == 0) and (self.denominator % i == 0 )):  
                GCD = i

        x=Fraction(self.numerator//GCD,self.denominator//GCD)
        return x
        


#Use example

a=Fraction(2,3)
a.Show()

b=Fraction(7,4)
b.Show()

h=a.Multiply(a,b)

c=Fraction(2,8)
print(c.ConvertFracToNum())

s=Fraction(24,6)
s.Simplify().Show()



