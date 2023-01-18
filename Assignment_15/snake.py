import random
import arcade

class Snake(arcade.Sprite):
    def __init__(self,game,ai):
        super().__init__()
        self.width=32
        self.height=35
        self.center_x=game.width//2
        self.center_y=game.height//2
        if ai:
            self.change_x=1
            self.change_y=0
        else:
            self.change_x=0
            self.change_y=0
        self.color=arcade.color.GREEN
        if ai==1:
            self.speed=1
        else:
            self.speed=2
        self.score=0
        self.body=[]

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        flg=0
        for part in self.body:
            if flg==0:
                arcade.draw_rectangle_filled(part['x'],part['y'],self.width,self.height,self.color)
                flg=1
            else:
                arcade.draw_rectangle_filled(part['x'],part['y'],self.width,self.height,arcade.color.BLUE)
                flg=0

    def move(self):
        self.center_x +=self.change_x*self.speed
        self.center_y +=self.change_y*self.speed
        self.body.append({'x':self.center_x,'y':self.center_y})
        
        if len(self.body) > self.score:
            print("body: ",len(self.body))
            print("score: ",self.score)
            self.body.pop(0)


    def eat(self,food,food_score):
        del food
        self.score+=food_score
        print(self.score)
       

