
print("=============================================================")
print("          ***    Welcome to List Inverter    ***")
print("=============================================================")

n=int(input("How many numbers would you like to enter? "))
list=[]
invert=[]
for i in range(n):
    list.append(int(input("Enter the number: ")))

for i in range(n-1,-1,-1):
    invert.append(list[i])
    print(list[i],end=" ")
