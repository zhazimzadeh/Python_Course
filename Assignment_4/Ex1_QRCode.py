import qrcode

print("=============================================================")
print("          ***    Welcome to QrCode Maker    ***")
print("=============================================================")

name=input(("Enter your name: "))
phone=input("Enter your phone number:")
img=qrcode.make(name + phone)
img.save("MyInfo.png")