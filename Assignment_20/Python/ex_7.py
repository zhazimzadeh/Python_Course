import random
import pyfiglet


def menu():
    

    choice = int(input("Enter your choice:"))
    while True:
        if choice == 1 :
            return "✋"
        elif choice == 2:
            return "🤚"
        else:
            choice = int(input("Try again: "))

#--------------------------------------------------#

user_win=0
comp1_win=0
comp2_win=0

for i in range(5):
        print("\nSelect one of them:")
        print("1. ✋")
        print("2. 🤚")
        user=int(input("Select: "))
        if user==1: print ("your choice: ✋")
        else:print ("your choice: 🤚")
        comp1 = random.choice([1,2])
        if comp1==1: print ("The choice of computer_1: ✋")
        else:print ("The choice of computer_1: 🤚")
        comp2 = random.choice([1,2])
        if comp2==1: print ("The choice of computer_2: ✋")
        else:print ("The choice of computer_2: 🤚")
        if user!= comp1 and user!=comp2:
            user_win+=1
        elif comp1!=user and comp1!=comp2:
            comp1_win+=1
        elif comp2!=user and comp2!=comp2:
            comp2_win+=1

if user_win>comp1_win and user_win>comp2_win:
    print("You Win!")
elif comp1_win>comp2_win:
    print("Computer_1 Win!")
elif comp2_win>comp1_win:
    print("Computer_2 Win!")




