import random  
import arcade
from spaceship import Spaceship
from enemy import Enemy




    
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=700,title="Interstellar game 2023")
        arcade.set_background_color(arcade.color.DARK_CERULEAN)
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=Spaceship(self.width)
        self.doshman=Enemy(self.width,self.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        self.doshman.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        print(symbol)
        if symbol==65361:
            print("left")
            self.me.center_x=self.me.center_x-self.me.speed
        elif symbol==65363:
            print("right")
            self.me.center_x=self.me.center_x+self.me.speed

    def on_update(self, delta_time: float):
        self.doshman.center_y-=self.doshman.speed


window=Game()
arcade.run()