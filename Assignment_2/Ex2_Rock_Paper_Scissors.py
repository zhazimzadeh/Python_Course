import random

while True:
    print("=========================================================")
    print("   ***    Welcome to Rock Paper Scissors Game    ***")
    print("=========================================================")

    print("Number 1 is Rock")
    print("Number 2 is Paper")
    print("Number 3 is Scissors")
    Computer_Num=random.randint(1,3)
    User_Num=int(input("What is your choice? : "))
 

    if(Computer_Num==User_Num):
        print("The choice of computer was similar to yours.The match is tied! 😐")

    elif(Computer_Num==1):
        if(User_Num==2):
            print("The choice of Computer was Rock.You Win! 🥳")
        else:
            print("The choice of Computer was Rock.You lose! 😭")

    elif(Computer_Num==2): 
        if(User_Num==1):
            print("The choice of Computer was Paper.You lose! 😭")
        else:
            print("The choice of Computer was Paper.You Win! 🥳")
       
    elif(Computer_Num==3):
        if(User_Num==1):
            print("The choice of Computer was Scissors.You Win! 🥳")
        else:
            print("The choice of Computer was Scissors.You lose! 😭")


        



