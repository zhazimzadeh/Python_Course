import random
import arcade

class br_Ball(arcade.Sprite):
    def __init__(self,rocket,pic):
        super().__init__(pic)
        self.center_x=rocket.center_x+10
        self.center_y=rocket.center_y+20
        self.change_x=random.choice([-1,0,1])
        self.change_y=1
        self.speed=4
        self.width=20
        self.height=20



    def move(self):
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed