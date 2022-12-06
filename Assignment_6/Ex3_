import math

print("=============================================================")
print("          ***    Welcome to Cubic equation    ***")
print("                 y=ax**3 +bx**2 +cx +d")
print("=============================================================")

while True:
    
    a=int(input("Enter a: "))
    while(a==0):
        a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=int(input("Enter c: "))
    d=int(input("Enter d: "))

    Delta=18*a*b*c*d-4*(b**3)*d+(b**2)*(d**2)-4*a*(c**3)-27*(a**2)*(d**2)
    Delta_0=b**2-3*a*c
    Delta_1=2*b**3-9*a*b*c+27*(a**2)*d
    Delta_12_4ac=-27*(a**2)*Delta

    C=((Delta_1+math.sqrt(Delta_12_4ac))/2)**(1/3)
    u=[1,complex(-1/2,math.sqrt(3)/2),complex(-1/2,-math.sqrt(3)/2)]
    x=[]
    for i in range(3):
        x.append(-1/(3*a)*(b+u[i]*C+Delta_0/(u[i]*C)))
        print("Root ",i,":" ,x[i])


