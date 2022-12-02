import math
print("==================================================")
print("      ***    Triangle Area     ***")
print("==================================================")

A=int(input("Input the first side of the triangle= "))
B=int(input("Input the second side of the triangle= "))
C=int(input("Input the third side of the triangle= "))

if(C<(A+B) and A<(C+B) and B<(A+C)):
    s=(int)(A+B+C)/2
    print("Triangle Area= ",math.sqrt(s*(s-A)*(s-B)*(s-C)) )
else:
    print("It is not possible to calculate the area of the triangle!" )




