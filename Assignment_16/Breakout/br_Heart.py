import arcade

class br_Heart(arcade.Sprite):
    def __init__(self,x,pic):
        super().__init__(pic)
        self.center_x=x
        self.center_y=20
        self.width=45
        self.height=10