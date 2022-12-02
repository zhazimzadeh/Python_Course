
print("==================================================")
print("      ***    Average Calculation     ***")
print("==================================================")
name=input("Type your first name= ")
Lname=input("Type your last name= ")
A=float(input("Input the first score= "))
B=float(input("Input the second score= "))
C=float(input("Input the third score= "))
avg=(A+B+C)/3
print("------------------------------------------------------------------")
if(avg>=17):
    print (name+" "+Lname+"'s average is ",avg," and the status is Great")
elif(avg>=12 and avg<17):
    print (name+" "+Lname+"'s average is ",avg," and the status is Normal")
elif(avg<12):
    print (name+" "+Lname+"'s average is ",avg," and the status is Failed")
print("------------------------------------------------------------------")