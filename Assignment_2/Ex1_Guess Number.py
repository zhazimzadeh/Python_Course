import random

while True:
    print("==================================================")
    print("      ***    Welcome to Guess Number Game     ***")
    print("==================================================")

    Guess_Cnt=0
    Computer_Num=random.randint(1,100)
    User_Num=int(input("You have 10 chances.Guess a number between 1 and 100: "))
    Guess_Cnt=Guess_Cnt+1
    for i in range(2,11):

        if(Computer_Num==User_Num):
            if(Guess_Cnt==1):
                print("✨You Win in your first guess 🥳✨")
            else:
                print("✨You Win after ", Guess_Cnt, "times✨")
            break

        else:
            if(User_Num<Computer_Num):
                print("Your guess is lower.Guess a greater number ⬆. The remain guess chances is", 10-Guess_Cnt)
                User_Num=int(input("Guess a number again: "))
                Guess_Cnt=Guess_Cnt+1
            else:
                print("Your guess is greater.Guess a lower number ⬇. The remain guess chances is", 10-Guess_Cnt)
                User_Num=int(input("Guess a number again: "))
                Guess_Cnt=Guess_Cnt+1

    if(Computer_Num!=User_Num):
        print("You lose😭. The correct Number is ", Computer_Num)




