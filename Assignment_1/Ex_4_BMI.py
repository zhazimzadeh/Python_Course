import math
print("==================================================")
print("      ***    BMI Calculation     ***")
print("==================================================")
w=float(input("Type your weight(Kg)= "))
h=float(input("Type your height(m)= "))
while (h==0):
    h=input("height cannot be zero.Type your height(m)= ")
bmi=w/(h*h)
print("------------------------------------------------------------------")
if(bmi<18.5):
    print("Your BMI is ",bmi," and you are underweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("Your BMI is ",bmi," and you are Normal weight")
elif(bmi>=25 and bmi<=29.9):
    print("Your BMI is ",bmi," and you are Overweight")
elif(bmi>=30 and bmi<=34.9):
    print("Your BMI is ",bmi," and you are Obesity")
elif(bmi>=35 and bmi<=39.9):
    print("Your BMI is ",bmi," and you are Extreme Obesity")
print("------------------------------------------------------------------")