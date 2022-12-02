print("=============================================================")
print("   ***    Welcome to Fibonacci sequence calculation    ***")
print("=============================================================")

while True:
    num1=0
    num2=1
    n=int(input ("\nPlease Enter number for Fibonacci sequence calculation: "))
    while(n<=0):
        n=int(input ("Please Enter number greater than 0: "))
    if(n==1):
        print(num1)
    else:
        for i in range(n):
            if(i==0):
                print(num2,end ="    ")
            else:
                fibo=num1+num2
                print(fibo ,end="    ")
                num1=num2
                num2=fibo

