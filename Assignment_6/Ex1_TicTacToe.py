import pyfiglet
from colorama import Fore, Style
import random
from timeit import default_timer as timer

Game_Array=[[" _ "," _ "," _ "],
            [" _ "," _ "," _ "],
            [" _ "," _ "," _ "]]

flg_valid=0
flg_win=0
cnt=0

def show():
    for row in Game_Array:
        for cell in row:
            if(cell=="X"):
                print(Fore.BLUE +" X ",end="")
            elif(cell=="O"):
                print(Fore.RED +" O ",end="")
            else:
                print(Fore.WHITE+cell,end="")
        print()

def Validate_check():
    flg_valid=0
    if 0<=row<=2 and 0<=col<=2 :
        if Game_Array[row][col]==" _ ":
            flg_valid=1
        else: flg_valid=0
    else:
        flg_valid=0
    return flg_valid

def Status_check():
    flg_win=0
    for i in range(3):
        if(Game_Array[i][0]!=" _ " and Game_Array[i][1]!=" _ " and Game_Array[i][2]!=" _ " and
           Game_Array[i][0]== Game_Array[i][1]==Game_Array[i][2] or
           Game_Array[0][i]!=" _ " and Game_Array[1][i]!=" _ " and Game_Array[2][i]!=" _ " and            
           Game_Array[0][i]== Game_Array[1][i]==Game_Array[2][i] ):        
                flg_win=1
                break

    if(flg_win==0):
        if( Game_Array[1][1]!= " _ "):
                if(Game_Array[0][0]== Game_Array[1][1]==Game_Array[2][2] or 
                    Game_Array[0][2]== Game_Array[1][1]==Game_Array[2][0] ):
                    flg_win=1
    return flg_win





Title=pyfiglet.figlet_format("Tic Tac Toe",font="Slant")
print(Title)

user_Choice=int(input("\n 1-Player vs CPU \n 2-Player vs Player\n Select your choice:"))
show()
time_start=timer()
while cnt<6:
    while True:
        print(Fore.BLUE+"Player 1 Turn:")
        row=(int(input("Row:")))
        col=(int(input("Col:")))
        flg_valid=Validate_check()
        if(flg_valid):
            Game_Array[row][col]="X"
            break
        else: print("The select position is Wrong!")

    show()
    cnt+=1
    if(cnt>2):
        flg_win=Status_check()
        if(flg_win):
            print("The player 1 Win!")
            break
    while True:
        if(user_Choice==2):
            print(Fore.RED+"Player 2 Turn:")
            row=(int(input("Row:")))
            col=(int(input("Col:")))
            flg_valid=Validate_check()
            if(flg_valid):
                Game_Array[row][col]="O"
                break
            else: print("The select position is Wrong!")
        else:
            flg_valid=0
            print(Fore.RED+"Computer Turn:")
            while(flg_valid==0):
                row=random.randint(0,2)
                col=random.randint(0,2)
                flg_valid=Validate_check()
            Game_Array[row][col]="O"
            break


    show()
    if(cnt>2):
        flg_win=Status_check()
        if(flg_win):
            if(user_Choice==2):print("The player 2 Win!")
            else:print("The Computer Win!")
            break

time_End=timer()
if(flg_win==0):
    "No one Wins!"

print("This game took", round(time_End-time_start,2) ,"Seconds")
