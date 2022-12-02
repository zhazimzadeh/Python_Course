
print("=========================================================")
print("   ***    Welcome to Second to time converter    ***")
print("=========================================================")

while True:
    UserTime=int(input("Enter seconds: "))
    hour=int(UserTime/3600)
    min=int((UserTime-hour*3600)/60)
    sec=int(UserTime-hour*3600-min*60)
    print("     ✨ Your time is", hour,":", min,":", sec  ,"✨" )


