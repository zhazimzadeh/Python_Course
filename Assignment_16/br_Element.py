import arcade

class br_Element(arcade.Sprite):
    def __init__(self,x,y,pic):
        super().__init__(pic)
        self.center_x=x
        self.center_y=y
        self.width=60
        self.height=20