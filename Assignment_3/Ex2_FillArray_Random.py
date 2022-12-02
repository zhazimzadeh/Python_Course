import random

while True:

    print("\n=============================================================")
    print("          ***    Welcome to Fill Array     ***")
    print("=============================================================")

    n=int(input("What is the lenght of your array? "))
    low=int(input("What number do you like as the lowest number? "))
    high=int(input("What number do you like as the highest number? "))
    my_array=[]
    print(" 🏳‍🌈 Your Array is ready:")
    for i in range(n):
        my_array.append(random.randint(low,high))
        print(my_array[i],end=",")
    
    