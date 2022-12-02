import random

Data = ["rose", "magazine", "newpaper", "water", "germany", "university",
        "flower", "beez", "truck", "glass", "mirror", "pant", "shoes", "body", 
        "freind","brother","sister","Daughter","john","paper","sweet","cook"]

while True:

    print("=============================================================")
    print("          ***    Welcome to Hangman Game    ***")
    print("=============================================================")

    word = random.choice(Data)
    Num_Guess = len(word)
    Num_Char_Word =Num_Guess
    TrueChar = []
    flg_Win=0

    while (Num_Guess > 0):
       
        Num_CorrectChar=0  

        for i in range(Num_Char_Word):
            if (word[i] in TrueChar):
                print(word[i], end = " ")
                Num_CorrectChar +=1
            else:                
                print('_', end = " ")
                
        if (Num_CorrectChar == Num_Char_Word):            
            print("\n ✨You win! 🥳")
            flg_Win=1
            break

        user_char = input("\nEnter one character: ").lower()

        while (len(user_char) != 1):
            user_char = input("Enter only one character! : ").lower()

        
        if (user_char in TrueChar):
            {}
        elif (user_char in word):
                    TrueChar.append(user_char)
                    print('✅')
        else:
                    Num_Guess -= 1
                    print('❌ the remain Chances: ' ,Num_Guess )
        
           

    if flg_Win == 0:
        print("\nGame Over! 🤕")
        print("The word was: ", word)