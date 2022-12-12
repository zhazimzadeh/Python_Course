import qrcode
from colorama import Fore

PRODUCTS = []

def read_From_Database():
    file = open("MyDataBase.txt", "r")
    for line in file:
        if(line!="\n"):
            result1 = line.split("\n")
            result = result1[0].split(",")
            MyDict = {"code":result[0], "name":result[1], "price":result[2], "count":result[3]}
            PRODUCTS.append(MyDict)    
    file.close()


def write_To_Database():
        file = open("MyDataBase.txt", "w")
        for product in PRODUCTS:
            file.write(product['code']+","+product['name']+","+product['price']+","+str(product['count'])+"\n")
        file.close()


def Show_menu():
   # title=pyfiglet.figlet_format("Welcome",font="slant")
    print(Fore.CYAN+"=========================================================")
    print(Fore.CYAN+"            ***    Welcome to My Stor    ***")
    print(Fore.CYAN+"=========================================================")  
    #print(title)
    print(Fore.CYAN+"1_ Add")
    print(Fore.CYAN+"2_ Edit")
    print(Fore.CYAN+"3_ Remove")
    print(Fore.CYAN+"4_ Search")
    print(Fore.CYAN+"5_ Show list")
    print(Fore.CYAN+"6_ Buy")
    print(Fore.CYAN+"7_ Make QR code")
    print(Fore.CYAN+"8_ Exit")
    print(Fore.WHITE)


def add():
    Code = input("Enter a code for product: ")
    while Code==0:
         Code = input("Enter a code for product: ")
    Name = input("Enter a name for product: ")
    while Name==0:
        Name = input("Enter a name for product: ")
    Price = input("Enter a price for product: ")
    Count = input("Enter number of the product: ")
    newProduct = {"code":Code, "name":Name, "price":Price, "count":Count}   
    PRODUCTS.append(newProduct)



def edit():
    
    code = input("\nEnter a product code to edit: ")
    find=show_List(0,code,0)
    if(find!=0):
            print()
            print("1. Name")
            print("2. Price")
            print("3. Count")
            user_input = int(input("Enter your choice to edit: "))
            
            if user_input == 1:
                find["name"] = input("Enter a new name: ")
                print("\nInformation updated successfully!")
                show_List(0,code,0)

            elif user_input == 2:
                find["price"] = input("Enter a price: ")
                print("\nInformation updated successfully!")
                show_List(0,code,0)

            elif user_input == 3:
                find["count"] = input("Enter number of the product: ")
                print("\nInformation updated successfully!")
                show_List(0,code,0)
    else:
        print("\n Information Was not found")




def remove():
    code = input("\nEnter a product code to remove: ")
    find=show_List(0,code,0)
    if(find!=0):
        PRODUCTS.remove(find)
        print("\nYour product has been removed successfully!")
    else:
        print("\nThe product was NOT found!")


def search():
    code = input("\nEnter a product code or its name to search: ")
    find=show_List(0,code,0)
    if(find==0):
        print("\nThe product was NOT found!")


def show_List(flg_all,code,name):
    print("----------------------------------------------------------")
    print("code\t\tname\t\tprice\t\tcount")
    print("----------------------------------------------------------")
    if flg_all:
        for product in PRODUCTS:
            print(product['code'],"\t\t",product['name'],"\t\t",product['price'],"\t\t",product['count'])
    else: 
        for product in PRODUCTS:
            if product["code"] == code or product["name"] == name:
                print(product['code'],"\t\t",product['name'],"\t\t",product['price'],"\t\t",product['count'])
                return product
        else:
            return 0


def buy():
    cart = []
    total_price = 0
    show_List(1,0,0)
    Choice="y"
    while Choice=="y":
        code = input("\nEnter the code to add your cart : ")
        for product in PRODUCTS:
            if product["code"] == code:
                num = int(input("Enter the number: "))
                if num <= int(product["count"]):   
                    new_Item =  {"code":product["code"], "name":product["name"], "price":product["price"], "count":num}                                                       
                    for item in cart:
                        if code == item["code"]:
                            item["count"] = int(item["count"]) + num                        
                            break    
                    else:               
                        cart.append(new_Item)
                    product["count"] = int(product["count"]) -int(new_Item["count"])
                    break
                else:
                    print("\nThis number of the product is Less than your number.")
                    break
        else:
            print("\nThe product was NOT found.")

        Choice = input("would you like to buy something else? y/n ").lower()


    if(len(cart)!=0):
        print("\nYour Bill:")
        print("------------------------------------------------------------------------")
        print("code\t\tname\t\tprice\t\tcount\t\tCost")
        print("------------------------------------------------------------------------")

        for item in cart:
            print(item['code'],"\t\t",item['name'],"\t\t",item['price'],"\t\t",item['count'],"\t\t",int(item['price']) * int(item['count']))
            total_price = total_price + int(item["price"])* int(item["count"])
        
        print("=========================================================================")
        
        print("Total Cost =", total_price)






def Make_QRcode():
    code = input("\nEnter a product code: ")

    for product in PRODUCTS:
        if product["code"] == code:
            image = qrcode.make(product['code']+product['name']+product['price']+product['count'])
            image.save(product['code']+".jpg")
            print("\nQR code was made successfully!")
            break
    else:
        print("The product was NOT found.")

    

read_From_Database()
print("Database is loading...")
while True:
    Show_menu()
    choice=int (input("enter your choice: "))
    print()
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_List(1,0,0)     
    elif choice == 6:
        buy()
    elif choice == 7:
        Make_QRcode()
    elif choice == 8:
        write_To_Database()
        exit()
    else:
        print("\nThe input isn't valid.\nTry again!")