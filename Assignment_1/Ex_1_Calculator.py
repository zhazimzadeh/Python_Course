import math
print("==================================================")
print("      ***    Welcome to my Calculator     ***")
print("==================================================")
print(" Operator            Description")
print(" -----------------------------------")
print("|   +    |       Addition           |")
print("|   -    |       Subtraction        |")
print("|   *    |       Multiplication     |")
print("|   /    |       Division           |")
print("|   ^    |       Exponentiation     |")
print("|   !    |       Factorial          |")
print("|  log   |       Logarithm          |")
print("|  sqrt  |       Sqrt               |")
print("|  cos   |       Cosine             |")
print("|  sin   |       Sine               |")
print("|  tan   |       Tangent            |")
print("|  cot   |       Arc tangent        |")

print(" ------------------------------------")
A=float(input("Press First number= "))
O=input("Type a math operation from the help table:   ")
if(O=="+" or O=="-"or O=="*"or O=="/" or O=="^"):
    B=float(input("Press second number= "))
    if(O=="+"):        
        result=A+B 
    elif(O=="-"):
        result=A-B 
    elif(O=="*"):
        result=A*B 
    elif(O=="/"):
        while(B==0):
            B=float(input("Zero is not valid.Press a valid number= "))
        result=A/B 
    elif(O=="^"):
        result=A^B 
    print(A,O,B," = ",result )
elif(O=="sqrt"):
    result=math.sqrt(A)
    print("sqrt(",A,")=",result)
elif(O=="!"):
    result=math.factorial(int(A))
    print("factorial(",A,")=",result)
elif(O=="log"):
    result=math.factorial(int(A))
    print("log(",A,")=",result)
elif(O=="sin"):
    result=math.sin(int(math.radians(A)))
    print("sin(",A,")=",result)
elif(O=="cos"):
    result=math.cos(int(math.radians(A)))
    print("cos(",A,")=",result)
elif(O=="tan"):
    result=math.tan(int(math.radians(A)))
    print("tan(",A,")=",result)
elif(O=="cot"):   
    result=math.tan(int(math.radians(A)))
    while(result==0):
            A=float(input("Number is not valid for arc tangent calculation.Press a valid number= "))
            result=math.tan(int(math.radians(A)))
    print("cot(",A,")=",result)





