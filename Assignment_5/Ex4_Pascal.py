print("=============================================================")
print("          ***    Welcome to Pascal Triangle    ***")
print("=============================================================")

n=int(input("Enter a Number for row:"))

Outp = []

for i in range(n):
    row = []  
    for j in range(i+1):
        if(j==0):
            row.append(1)
        elif(i!=0):
            if(j==i):
                row.append(Outp[i-1][j-1])
            else:
                row.append(Outp[i-1][j-1]+Outp[i-1][j])               
        else:
            break
    Outp.append(row)

for i in Outp:
    print(i)

