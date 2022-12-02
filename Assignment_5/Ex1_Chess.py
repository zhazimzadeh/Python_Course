print("=============================================================")
print("          ***    Welcome to Print Chess paper    ***")
print("=============================================================")

n=int(input("Enter the number of row: "))
m=int(input("Enter the number of Column: "))

flg_row=0
flg_col=0
for i in range(n):
    for j in range(m):
        if(flg_row==0):
            if(flg_col==0):
                flg_col=1
                print("*",end="")
            else: 
                flg_col=0 
                print("#",end="")
        else:
            if(flg_col==0):
                flg_col=1
                print("#",end="")
            else: 
                flg_col=0 
                print("*",end="")
    print("")
    if(flg_row==0): 
        flg_row=1
    else: flg_row=0

