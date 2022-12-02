
while True:

    print("\n=============================================================")
    print("          ***    Welcome to Get Array     ***")
    print("=============================================================")

    n=int(input("What is the lenght of your array? "))
    my_array=[]

    flg_sort=1
    for i in range(n):
        my_array.append(int(input("enter a number: ")))
        if(i>0):
            if(my_array[i-1]> my_array[i]):
                flg_sort=0

    if(flg_sort):
        print(" Your array is sorted in ascending order ⬆")
    else:
        print(" Your array is not sorted!")

    