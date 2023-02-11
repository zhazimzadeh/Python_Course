import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.center_x=game.width//2
        self.center_y=game.height//2
        self.change_x=random.choice([-1,1])
        self.change_y=random.choice([-1,1])
        self.speed=5
        self.width=20
        self.height=20


    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,10,arcade.color.CYAN)

    def move(self):
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed