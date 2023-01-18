import random
import arcade



class Apple(arcade.Sprite):
    def __init__(self,game,pic):
        super().__init__(pic)
        self.width=38
        self.height=38
        self.center_x=random.randint(random.randint(38,game.width//2-38),
                                    random.randint(game.width//2+38,game.width-38))
       
        self.center_y=random.randint(random.randint(38,game.height//2-38),
                                    random.randint(game.height//2+38,game.height-38))

        self.change_x=0
        self.change_y=0
