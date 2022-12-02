print("=============================================================")
print("          ***    Welcome to Multiplication table    ***")
print("=============================================================")

n=int(input("Enter the number of row: "))
m=int(input("Enter the number of Column: "))


for i in range(n+1):
    for j in range(m+1):
        if(i==0):
            if(j==0):
                print("X",end=" ")
            else:
                print(j,end=" ")
        elif(j==0):
                print(i,end=" ")
        else: 
            print(i*j,end=" ")
    print("")
   
