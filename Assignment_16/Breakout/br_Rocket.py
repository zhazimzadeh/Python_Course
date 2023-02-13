import arcade


class br_Rocket(arcade.Sprite):
    def __init__(self,w,pic) :
        super().__init__(pic)
        self.center_x=w//2
        self.center_y=80
        self.width=90
        self.height=20
        self.speed=4
        self.change_x=0
        self.change_y=0
        self.game_width=w


    def move(self):
        if(self.change_x==-1):
            if(self.center_x>0):
                self.center_x -=self.speed
        elif(self.change_x==1):
            if(self.center_x<self.game_width):
                self.center_x +=self.speed


