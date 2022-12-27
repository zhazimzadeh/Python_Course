n=int(input("Please Enter n: "))

if(n%2==0):
    print("Your number is even")
else:
    for i in range(n):
        for j in range(n):
            if(i%2==0):
                if(j%2==0):
                    print("🤍",end="")
                else:
                    print("🖤",end="")
            else:
                if(j%2==0):
                    print("🖤",end="")
                else:
                    print("🤍",end="")
        print()
