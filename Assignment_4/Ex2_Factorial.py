
print("=============================================================")
print("          ***    Welcome to QrCode Maker    ***")
print("=============================================================")

Num = int(input("Enter a number: "))

result=1
cnt=2

while result < Num:
    result = result*cnt
    cnt+=1

if result == Num:
    print("😊",Num," is a factorial number")
else:
    print("😕",Num," is not a factorial number")