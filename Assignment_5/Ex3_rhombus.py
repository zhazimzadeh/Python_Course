print("=============================================================")
print("          ***    Welcome to Draw a Rhombus    ***")
print("=============================================================")

n=int(input("Enter a Number:"))
print()

for i in range(n):
    for j in range(n*2):
        if(n-i<=j<=n+i):
            print("*",end="")
        else: 
            print(" ",end="")
    print()
   

for i in range(n):
    for j in range(n*2):
        if(i+1<j<n*2-i-1):
            print("*",end="")
        else: 
            print(" ",end="")
    print()