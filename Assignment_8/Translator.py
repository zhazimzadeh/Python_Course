from colorama import Fore
import gtts
import os
import imageio

def read_from_file():
    global Word_bank
    result=os.listdir("Assignment_8")
    if("translate.txt")not in result:
        return 0
    print(result)
    file=open("Assignment_8/translate.txt","r")
    f=file.read().split("\n")
    Word_bank=[]
    for i in range(0,len(f),2):
        if(i!="\n" and i+1<len(f)):
            My_Dict={"en":f[i],"fa":f[i+1]}
            Word_bank.append(My_Dict)
    file.close()

def show_menu():
    print(Fore.CYAN+"=========================================================")
    print("            ***    Welcome to Translator    ***")
    print("=========================================================")  
    print("1_Translate English to Persian")
    print("2_Translate Persian to English")
    print("3_Add New Word")
    print("4_exit")
    print(Fore.WHITE+"\n")

def Translate_English_Farsi():
    user_text=input("enter an english word/sentence: ")
    user_word=user_text.split(" ")
    output=""
    for user_W in user_word:
        for word in Word_bank:
            if user_W==word["en"]:
                output=output+ word["fa"]+" "
                break
        else:
            output=output+user_W+" "
    print (output) 
    temp_Sound=gtts.gTTS(output,lang="ar",slow=False)
    temp_Sound.save("Assignment_8/sound_ar.mp3")

def Translate_Farsi_English():
    user_text=input("enter a Persian word/sentence: ")
    user_word=user_text.split(" "or".")
    output=""
    for user_W in user_word:
        for word in Word_bank:
            if user_W==word["fa"]:
                output=output+ word["en"]+" "
                break
        else:
            output=output+user_W+" "
    print (output) 
    temp_Sound=gtts.gTTS(output,lang="en",slow=False)
    temp_Sound.save("Assignment_8/sound_en.mp3")

    

def Add():
    English_word=input("Enter a new English Word:")
    Persian_Word=input("Enter a new Persian Word:")
    NewItem={"en":English_word,"fa":Persian_Word}
    Word_bank.append(NewItem)
    print("Your words were added Successfully!")

def Write_to_Dictionary():
        file = open("Assignment_8/translate.txt", "w")
        for word in Word_bank:
            file.write(word['en']+"\n"+word['fa'] +"\n")
        file.close()

if(read_from_file()==0):
    print(Fore.RED+"there is no Dictionary file in the path ")
else:
    while True:
        show_menu()
        
        choice=int(input("Enter your choice:"))
        if(choice==1):
            Translate_English_Farsi()
        elif(choice==2):
            Translate_Farsi_English()
        elif(choice==3):
            Add()
        else:
            Write_to_Dictionary()
            exit(0)




     



