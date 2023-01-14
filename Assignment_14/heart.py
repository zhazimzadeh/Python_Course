import arcade

class Heart(arcade.Sprite):
    def __init__(self,x):
        super().__init__("Assignment_14\heart.png")
        self.center_x=x
        self. center_y=10
        self.width=20
        self.height=20