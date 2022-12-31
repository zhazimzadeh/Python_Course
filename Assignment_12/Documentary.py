from Media import Media
from Actor import Actor

class Documentary(Media):
    def __init__(self, type, id, name, director, IMDBscore, url, duration, casts,subject):
        super().__init__(type, id, name, director, IMDBscore, url, duration, casts)
        
        self.subject=subject

    def show(self):
        self.showInfo()
        print("subject: ",self.subject)
        print("------------------------------------------------------------------------")


    def edit(self):
                print()
                print("1. Name")
                print("2. Director")
                print("3. IMDBscore")
                print("4. url")
                print("5. duration")
                print("6. subject")
                print("7. casts")

                user_input = int(input("Enter your choice to edit: "))
                
                if user_input == 1:
                    self.name = input("Enter a new name: ")
                    print("\nInformation updated successfully!")
                    

                elif user_input == 2:
                    self.director = input("Enter a new director: ")
                    print("\nInformation updated successfully!")
                    
                elif user_input == 3:
                    self.IMDBscore = input("Enter a new score: ")
                    print("\nInformation updated successfully!")

                elif user_input == 4:
                    self.url = input("Enter a new URL: ")
                    print("\nInformation updated successfully!")

                elif user_input == 5:
                    self.duration = input("Enter a new duration: ")
                    print("\nInformation updated successfully!")

                elif user_input == 6:
                    self.subject = input("Enter a new subject: ")
                    print("\nInformation updated successfully!")

                elif user_input==7:
                    actors=[]

                    choice=input("Do you want to delete casts and enter again?")
                    if choice.lower()=="y":
                        n=int(input("Enter the number of actors:"))
                        for i in range(n):
                            actor=Actor(0,0)
                            actor.name=input("Enter name: ")
                            actor.age=input("Enter age: ")
                            actors.append(actor)
                        self.casts=actors