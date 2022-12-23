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
        ...

    def Add(self):
        ...

    def Subtract(self, other):
        ...

    def Multiply(self):
        ...

    def Divide(self):
        ...
    
    def Rounding():
        ...

    def Compare():
        ...
