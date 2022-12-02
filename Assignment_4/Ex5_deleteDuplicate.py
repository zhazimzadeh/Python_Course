
print("=============================================================")
print("          ***    Welcome to Delete Dupicate number    ***")
print("=============================================================")
n=int(input("How many numbers would you like to enter? "))
list=[]
NoDuplicate=[]
for i in range(n):
    list.append(int(input("Enter the number: ")))
    if list[i] not in NoDuplicate:
        NoDuplicate.append(list[i])

print("The numbers without duplicate are: ")
for i in NoDuplicate:
    print(i,end=" ")


