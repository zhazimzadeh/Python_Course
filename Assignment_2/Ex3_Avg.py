


print("=========================================================")
print("   ***    Welcome to Average calculation    ***")
print("=========================================================")
print("you can type 'exit' to close this program") 
sum=0
num_cnt=0
while True:
    Score=input("Enter your Score:")

    if(Score=="exit"):
        break
    else:
        sum=sum+int(Score)
        num_cnt=num_cnt+1
        print("         ✨ Your Average is",sum/num_cnt ,"✨")





