while True:

    print("\n=============================================================")
    print("          ***    Welcome to Create Snake     ***")
    print("=============================================================")

    n=int(input("What is the lenght of your Snake? "))

    flg=0
    for i in range(n):
        if(flg):
            flg=0
            print("#", end="")
        else:
            flg=1
            print("*", end="")