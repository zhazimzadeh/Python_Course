from colorama import Fore

from Film import Film
from Series import Series
from Documentary import Documentary
from Clip import Clip
from Media import Media
from Actor import Actor


cart = []
PRODUCTS = []
MEDIA=[]


class Products:
    def __init__(self, id,name,price,count):
        self.id=id
        self.name=name
        self.price=price
        self.count=count

    @staticmethod
    def add():
        id = input("Enter a code for product: ")
        while id==0:
            id = input("Enter a code for product: ")
        Name = input("Enter a name for product: ")
        while Name==0:
            Name = input("Enter a name for product: ")
        Price = input("Enter a price for product: ")
        Count = input("Enter number of the product: ")
        newProduct = Products(id,Name,Price,Count)   
        PRODUCTS.append(newProduct)

    def edit(self):
                print()
                print("1. Name")
                print("2. Price")
                print("3. Count")
                user_input = int(input("Enter your choice to edit: "))
                
                if user_input == 1:
                    self.name = input("Enter a new name: ")
                    print("\nInformation updated successfully!")
                    

                elif user_input == 2:
                    self.price = input("Enter a price: ")
                    print("\nInformation updated successfully!")
                    

                elif user_input == 3:
                    self.count = input("Enter number of the product: ")
                    print("\nInformation updated successfully!")
                    
    def remove(self):
            PRODUCTS.remove(self)
            print("\nYour product has been removed successfully!")

    @staticmethod
    def search():
        code = input("\nEnter a product code or its name to search: ")
        find=Products.show_List(0,code,code)
        if(find==0):
            print("\nThe product was NOT found!")


    def buy(self,num):
        new_Item =  Products(self.id, self.name, self.price, num) 
        if(len(cart)==0):
            cart.append(new_Item)
            self.count = int(self.count) -int(new_Item.count)    
        else:                                                  
            for item in cart:
                if code == item.id:
                    item.count = int(item.count) + num                        
                    break    
                else:               
                    cart.append(new_Item)
                    self.count = int(self.count) -int(new_Item.count)
                    break

    @staticmethod
    def Print_Bill():
        total_price=0
        if(len(cart)!=0):
            print("\nYour Bill:")
            print("------------------------------------------------------------------------")
            print("code\t\tname\t\tprice\t\tcount\t\tCost")
            print("------------------------------------------------------------------------")

            for item in cart:
                print(item.id,"\t\t",item.name,"\t\t",item.price,"\t\t",item.count,"\t\t",int(item.price) * int(item.count))
                total_price = total_price + int(item.price)* int(item.count)
            
            print("=========================================================================")
            
            print("Total Cost =", total_price)

    @staticmethod
    def show_List(flg_all,code,name):
        print("----------------------------------------------------------")
        print("code\t\tname\t\tprice\t\tcount")
        print("----------------------------------------------------------")
        if flg_all:
            for product in PRODUCTS:
                print(product.id,"\t\t",product.name,"\t\t",product.price,"\t\t",product.count)
        else: 
            for product in PRODUCTS:
                if product.id == code or product.name == name:
                    print(product.id,"\t\t",product.name,"\t\t",product.price,"\t\t",product.count)
                    return product
            else:
                return 0

class Database:
    def __init__(self):
        ...

    def read_From_Database(self):
        file = open("G:\Python\online_course\Python_Course\Assignment_12\MyDataBase.txt", "r")
        for line in file:
            if(line!="\n"):
                result1 = line.split("\n")
                result = result1[0].split(",")
                my_object=Products(result[0],result[1],result[2],result[3])
                PRODUCTS.append(my_object)    
        file.close()

        file = open("G:\Python\online_course\Python_Course\Assignment_12\Media_DataBase.txt", "r")
        for line in file:
            if(line!="\n"):
                result1 = line.split("\n")
                result = result1[0].split(",")
                ACTOR=[]

                if(int(result[0])==0):  #Type film
                    my_object=Film(0,0,0,0,0,0,0,0,0)
                    my_object.type="0"
                    my_object.id=result[1]
                    my_object.name=result[2]
                    my_object.director=result[3]
                    my_object.IMDBscore=result[4]
                    my_object.url=result[5]
                    my_object.duration=result[6]
                    my_object.year=result[7]
                    for  i in range(8,len(result)-1,2):
                            actor=Actor(result[i],result[i+1])
                            ACTOR.append(actor)
                    my_object.casts=ACTOR
                elif(int(result[0])==1):  #Type Series 
                    my_object=Series(0,0,0,0,0,0,0,0,0)
                    my_object.type="1"
                    my_object.id=result[1]
                    my_object.name=result[2]
                    my_object.director=result[3]
                    my_object.IMDBscore=result[4]
                    my_object.url=result[5]
                    my_object.duration=result[6]
                    my_object.episode=result[7]
                    for  i in range(8,len(result)-1,2):
                            actor=Actor(result[i],result[i+1])
                            ACTOR.append(actor)
                    my_object.casts=ACTOR
                elif(int(result[0])==2):  #Type Documentary 
                    my_object=Documentary(0,0,0,0,0,0,0,0,0)
                    my_object.type="2"
                    my_object.id=result[1]
                    my_object.name=result[2]
                    my_object.director=result[3]
                    my_object.IMDBscore=result[4]
                    my_object.url=result[5]
                    my_object.duration=result[6]
                    my_object.subject=result[7]
                    for  i in range(8,len(result)-1,2):
                            actor=Actor(result[i],result[i+1])
                            ACTOR.append(actor)
                    my_object.casts=ACTOR
                elif(int(result[0])==3):  #Type Clip 
                    my_object=Clip(0,0,0,0,0,0,0,0,0)
                    my_object.type="3"
                    my_object.id=result[1]
                    my_object.name=result[2]
                    my_object.director=result[3]
                    my_object.IMDBscore=result[4]
                    my_object.url=result[5]
                    my_object.duration=result[6]
                    my_object.subject=result[7]
                    for  i in range(8,len(result)-1,2):
                            actor=Actor(result[i],result[i+1])
                            ACTOR.append(actor)
                    my_object.casts=ACTOR

                MEDIA.append(my_object)    
        file.close()


    def write_To_Database(self):
            file = open("G:\Python\online_course\Python_Course\Assignment_12\MyDataBase.txt", "w")
            for product in PRODUCTS:
                file.write(product.id+","+product.name+","+product.price+","+str(product.count)+"\n")
            file.close()

            file = open("G:\Python\online_course\Python_Course\Assignment_12\Media_DataBase.txt", "w")
            for media in MEDIA:
                if(int(media.type)==0) :  
                    file.write(media.type+","+media.id+","+media.name+","+media.director+","+media.IMDBscore+","+media.url+","+media.duration+","+media.year)
                    for a in media.casts:   
                        file.write(","+a.name+","+a.age)
                    file.write("\n")
                elif(int(media.type)==1) : 
                    file.write(media.type+","+media.id+","+media.name+","+media.director+","+media.IMDBscore+","+media.url+","+media.duration+","+media.episode)
                    for a in media.casts:   
                            file.write(","+a.name+","+a.age)
                    file.write("\n")
                elif(int(media.type)==2 or int(media.type)==2) :
                    file.write(media.type+","+media.id+","+media.name+","+media.director+","+media.IMDBscore+","+media.url+","+media.duration+","+media.subject)
                    for a in media.casts:   
                        file.write(","+a.name+","+a.age)
                    file.write("\n")
 
            file.close()

def Show_main_menu():
    print(Fore.WHITE+"=========================================================")
    print(Fore.WHITE+"            ***    Welcome to My Store    ***")
    print(Fore.WHITE+"=========================================================")  

    print(Fore.CYAN+"1_ Media Store")
    print(Fore.CYAN+"2_ Product Store")
    print(Fore.CYAN+"3_ Exit")
    print(Fore.WHITE)

def Show_product_menu():
   # title=pyfiglet.figlet_format("Welcome",font="slant")
    print(Fore.CYAN+"=========================================================")
    print(Fore.CYAN+"            ***    Welcome to My Product Store    ***")
    print(Fore.CYAN+"=========================================================")  
    #print(title)
    print(Fore.CYAN+"1_ Add")
    print(Fore.CYAN+"2_ Edit")
    print(Fore.CYAN+"3_ Remove")
    print(Fore.CYAN+"4_ Search")
    print(Fore.CYAN+"5_ Show list")
    print(Fore.CYAN+"6_ Buy")
    print(Fore.CYAN+"7_ Exit")
    print(Fore.WHITE)

def Show_media_menu():
   # title=pyfiglet.figlet_format("Welcome",font="slant")
    print(Fore.CYAN+"=========================================================")
    print(Fore.CYAN+"            ***    Welcome to My Media Store    ***")
    print(Fore.CYAN+"=========================================================")  
    #print(title)
    print(Fore.CYAN+"1_ Add")
    print(Fore.CYAN+"2_ Edit")
    print(Fore.CYAN+"3_ Remove")
    print(Fore.CYAN+"4_ Show list")
    print(Fore.CYAN+"5_ Search by time")
    print(Fore.CYAN+"6_ download")
    print(Fore.CYAN+"7_ Exit")
    print(Fore.WHITE)

db=Database()
db.read_From_Database()
while True:
    Show_main_menu()
    choice=int (input("enter your choice: "))
    if choice==1:
        Show_media_menu()
        choice=int (input("enter your choice: "))
        print()
        if choice==1:
            
            print("1_Film\n2_Series\n3_Documentary\n4_Clip\n")
            n=int(input("Please choose to add:"))
            if(n==1):
                    ACTOR=[]
                    my_object=Film(0,0,0,0,0,0,0,0,0)
                    my_object.type="0"
                    my_object.id=input("Enter a code: ")
                    my_object.name=input("Enter a name: ")
                    my_object.director=input("Enter a director: ")
                    my_object.IMDBscore=input("Enter IMDB score: ")
                    my_object.url=input("Enter a url: ")
                    my_object.duration=input("Enter the duration(min): ")
                    my_object.year=input("Year: ")
                    n=int(input("Enter the number of actors:"))
                    for i in range(n):
                        actor=Actor(0,0)
                        actor.name=input("Enter name: ")
                        actor.age=input("Enter age: ")
                        ACTOR.append(actor)
                    my_object.casts=ACTOR
                    MEDIA.append(my_object)
            elif(n==2):
                    ACTOR=[]
                    my_object=Series(0,0,0,0,0,0,0,0,0)
                    my_object.type="1"
                    my_object.id=input("Enter a code: ")
                    my_object.name=input("Enter a name: ")
                    my_object.director=input("Enter a director: ")
                    my_object.IMDBscore=input("Enter IMDB score: ")
                    my_object.url=input("Enter a url: ")
                    my_object.duration=input("Enter the duration(min): ")
                    my_object.episode=input("Episodes: ")
                    n=int(input("Enter the number of actors:"))
                    for i in range(n):
                        actor=Actor(0,0)
                        actor.name=input("Enter name: ")
                        actor.age=input("Enter age: ")
                        ACTOR.append(actor)
                    my_object.casts=ACTOR
                    MEDIA.append(my_object)
            elif(n==3):
                    ACTOR=[]
                    my_object=Documentary(0,0,0,0,0,0,0,0,0)
                    my_object.type="2"
                    my_object.id=input("Enter a code: ")
                    my_object.name=input("Enter a name: ")
                    my_object.director=input("Enter a director: ")
                    my_object.IMDBscore=input("Enter IMDB score: ")
                    my_object.url=input("Enter a url: ")
                    my_object.duration=input("Enter the duration(min): ")
                    my_object.subject=input("subject: ")
                    n=int(input("Enter the number of actors:"))
                    for i in range(n):
                        actor=Actor(0,0)
                        actor.name=input("Enter name: ")
                        actor.age=input("Enter age: ")
                        ACTOR.append(actor)
                    my_object.casts=ACTOR
                    MEDIA.append(my_object)
            elif(n==4):
                    ACTOR=[]
                    my_object=Clip(0,0,0,0,0,0,0,0,0)
                    my_object.type="3"
                    my_object.id=input("Enter a code: ")
                    my_object.name=input("Enter a name: ")
                    my_object.director=input("Enter a director: ")
                    my_object.IMDBscore=input("Enter IMDB score: ")
                    my_object.url=input("Enter a url: ")
                    my_object.duration=input("Enter the duration(min): ")
                    my_object.subject=input("subject: ")
                    n=int(input("Enter the number of actors:"))
                    for i in range(n):
                        actor=Actor(0,0)
                        actor.name=input("Enter name: ")
                        actor.age=input("Enter age: ")
                        ACTOR.append(actor)
                    my_object.casts=ACTOR
                    MEDIA.append(my_object)
            print("\n Information was added!")
        elif choice == 2:
            code = input("\nEnter a Media code to edit: ")
            for m in MEDIA:
                if m.id == code:
                    m.show()
                    m.edit()
                    print("\n Information was edited!")
                    break
            else:
                print("\n Information Was not found")
        elif choice == 3:
            code = input("\nEnter a media code to remove: ")
            for m in MEDIA:
                if m.id == code:
                    m.show()
                    MEDIA.remove(m)
                    print("\n Information was deleted!")
                    break
            else:
                print("\n Information Was not found")    
        elif choice == 4:
            for m in MEDIA:
                m.show()
        elif choice==5:
            min1=int(input("Please Enter the first time: "))
            min2=int(input("Please Enter the second time: "))
            for m in MEDIA:
                if(int(m.duration)>=min1 and int(m.duration)<=min2):
                    m.show()
                

        elif choice==6:
            code = input("\nEnter a Media code to download: ")
            for m in MEDIA:
                if m.id == code:
                    m.download()
            else:
                print("\n Information Was not found")
        elif choice==7:
            db.write_To_Database()
            exit()
        else:
            print("\nThe input isn't valid.\nTry again!")

    elif choice==2:
        Show_product_menu()
        choice=int (input("enter your choice: "))
        print()
        if choice == 1:
            Products.add()
        elif choice == 2:
            code = input("\nEnter a product code to edit: ")
            for product in PRODUCTS:
                if product.id == code:
                    print(product.id,"\t\t",product.name,"\t\t",product.price,"\t\t",product.count)
                    product.edit()
                    break
            else:
                print("\n Information Was not found")

        elif choice == 3:
            code = input("\nEnter a product code to remove: ")
            for product in PRODUCTS:
                if product.id == code:
                    print(product.id,"\t\t",product.name,"\t\t",product.price,"\t\t",product.count)
                    product.remove()
                    break
            else:
                print("\n Information Was not found")
        elif choice == 4:
            Products.search()
        elif choice == 5:
            Products.show_List(1,0,0)     
        elif choice == 6:             
            total_price = 0
            Products.show_List(1,0,0)
            Choice="y"
            while Choice=="y":
                code = input("\nEnter the code to add your cart : ")
                for product in PRODUCTS:
                    if product.id == code:
                        num = int(input("Enter the number: "))
                        if num <= int(product.count):   
                            product.buy(num)
                            break
                        else:
                            print("\nThis number of the product is Less than your number.")
                            break
                else:
                    print("\n  the information was not found")
                Choice = input("would you like to buy something else?(y/n) ").lower()
            Products.Print_Bill()


        elif choice == 7:
            db.write_To_Database()
            exit()
        else:
            print("\nThe input isn't valid.\nTry again!")
    elif choice==3:
        db.write_To_Database()
        exit()
    else:
            print("\nThe input isn't valid.\nTry again!")