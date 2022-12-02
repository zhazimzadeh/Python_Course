while True:

    print("\n=============================================================")
    print("          ***    Welcome to LCM Calculation     ***")
    print("=============================================================")

    num1 = int(input("Enter the first Number = "))
    num2 = int(input("Enter the second Number = "))
    GCD = 0
    x=max(num1,num2)
    for i in range(1, x + 1):  
        if (( num1 % i == 0) and (num2 % i == 0 )):  
            GCD = i

    print(" LCM =", int(num1 * num2 /GCD))