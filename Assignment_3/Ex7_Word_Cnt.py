while True:

    print("\n=============================================================")
    print("          ***    Welcome to Word Counter     ***")
    print("=============================================================")

    Sentence = input("Enter Your Word or Sentence : ")
    cnt=1
    flg1=1
    if(len(Sentence)>0):
        for i in range(len(Sentence)):  
            if(i<len(Sentence)-1):
                if (Sentence[i]!=" " ):
                    flg1=0
                    if(Sentence[i+1]==" " ):  
                        cnt +=1  
                 
                          
    else: cnt=0
    if(flg1): cnt=1
    if(cnt>0):
        print("The number of words in your Sentence is: ", cnt)