n=int(input("What is the lenght of your array? "))
my_array=[]

flg_symmetry=1
for i in range(n):
        my_array.append(int(input("enter a number: ")))
i=0
if n%2==0:
    for i in range(n//2):
        if(my_array[i]!= my_array[n-i-1]):
            flg_symmetry=0
            break
else:
    for i in range(n//2):
        if(my_array[i]!= my_array[n-i-1]):
            flg_symmetry=0
            break


if(flg_symmetry):
        print(" Your array is symmetry")
else:
        print(" Your array is not symmetry!")
