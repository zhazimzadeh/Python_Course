import qrcode
from colorama import Fore
import sqlite3



def db():
    global con
    global cur
    con=sqlite3.connect("Assignment_21\store.db")
    cur=con.cursor()



def Show_menu():
   # title=pyfiglet.figlet_format("Welcome",font="slant")
    print(Fore.CYAN+"=========================================================")
    print(Fore.CYAN+"            ***    Welcome to My Store    ***")
    print(Fore.CYAN+"=========================================================")  
    #print(title)
    print(Fore.CYAN+"1_ Add")
    print(Fore.CYAN+"2_ Edit")
    print(Fore.CYAN+"3_ Remove")
    print(Fore.CYAN+"4_ Search")
    print(Fore.CYAN+"5_ Show list")
    print(Fore.CYAN+"6_ Buy")
    print(Fore.WHITE)


def add():
    global con
    global cur
    Name = input("Enter a name for product: ")
    while Name==0:
        Name = input("Enter a name for product: ")
    Price = input("Enter a price for product: ")
    Count = input("Enter number of the product: ")
    cur.execute(f"insert into product (name,price,count) VALUES('{Name}',{Price},{Count})")
    con.commit()



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
                name = input("Enter a new name: ")
                cur.execute(f"update product set name='{name}' where id={find[0]}")
                con.commit()
                print("\nInformation updated successfully!")
                show_List(0,code,0)

            elif user_input == 2:
                price = input("Enter a price: ")
                cur.execute(f"update product set price={price} where id={find[0]}")
                con.commit()
                print("\nInformation updated successfully!")
                show_List(0,code,0)

            elif user_input == 3:
                count = input("Enter number of the product: ")
                cur.execute(f"update product set count={count} where id={find[0]}")
                con.commit()
                print("\nInformation updated successfully!")
                show_List(0,code,0)
    else:
        print("\n Information Was not found")




def remove():
    code = input("\nEnter a product code to remove: ")
    find=show_List(0,code,0)
    if(find!=0):
        cur.execute(f"delete from product where id={find[0]}")
        con.commit()
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
    resutl=cur.execute("select * from product")
    tb=resutl.fetchall()
    if flg_all:
        for product in tb:
            print(product[0],"\t\t",product[1],"\t\t",product[2],"\t\t",product[3])
    else: 
        for product in tb:
            if product[0] == int(code) or product[1] == name:
                print(product[0],"\t\t",product[1],"\t\t",product[2],"\t\t",product[3])
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
        tb=cur.execute(f"select * from product where id={code}")
        result=tb.fetchall()

        if result!=[]:
                num = int(input("Enter the number: "))
                if num <= int(result[0][3]):   
                    new_Item =  {"code":result[0][0], "name":result[0][1], "price":result[0][2], "count":num}                                                       
                    for item in cart:
                        if int(code) == item["code"]:
                            item["count"] = int(item["count"]) + num                        
                            break    
                    else:               
                        cart.append(new_Item)
                    newcount=int(result[0][3]) -int(new_Item["count"])
                    cur.execute(f"update product set count ={newcount} where id={code}")
                    con.commit()
                    # result[0][3] = int(result[0][3]) -int(new_Item["count"])
                    # break
                else:
                    print("\nThis number of the product is Less than your number.")
                    # break
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




db()

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
    else:
        print("\nThe input isn't valid.\nTry again!")