from timeit import default_timer as timer
import arcade
from ball import Ball
from rocket import Rocket


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=500,title="My Pong 🏓",center_window=True)
        arcade.set_background_color(arcade.color.DARK_GREEN)
        

        self.ball=Ball(self)
        self.Player_1=Rocket(40,self.height//2,arcade.color.YELLOW,"A")
        self.Player_2=Rocket(self.width-40,self.height//2,arcade.color.RED,"B")
        self.gameOver=0



    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(self.width//2,self.height//2,self.width-10,self.height-10,arcade.color.WHITE,border_width=10)
        arcade.draw_line(self.width//2,20,self.width//2,self.height-20,arcade.color.WHITE,10)
        self.Player_1.draw()
        self.Player_2.draw()
        self.ball.draw()



        if self.gameOver==1:
            arcade.draw_rectangle_filled(0,0,self.width*2,self.height*2,arcade.color.BLACK)
            # arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over!",self.width//2-70,self.height//2,arcade.color.WHITE,25)          

            a=timer()
            if(int(timer()-a)>10):
                # del self.apple
                # del self.pear 
                # del self.shit
                # del self.snake 
                exit(0)

        if self.gameOver==0:
            # self.apple.draw()
            # self.shit.draw()
            # self.pear.draw()
            # self.snake.draw()
            arcade.draw_text(self.Player_1.score,30,20,arcade.color.YELLOW,30)
            arcade.draw_text(self.Player_2.score,self.width-50,20,arcade.color.RED,30)
            
        
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.Player_1.height <y <self.height-self.Player_1.height:
             self.Player_1.center_y=y

        

    def on_update(self, delta_time: float):
        if(self.gameOver==0):
            self.ball.move()

            self.Player_2.move(self.ball,self)
            if self.ball.center_y <30 or self.ball.center_y>self.height-30:
                self.ball.change_y *=-1

            
            if arcade.check_for_collision(self.Player_1,self.ball) or \
                 arcade.check_for_collision(self.Player_2,self.ball):
                self.ball.change_x*=-1

            if self.ball.center_x<0:
                self.Player_2.score+=1
                del self.ball
                self.ball=Ball(self)
                
            if self.ball.center_x>self.width:
                self.Player_1.score+=1
                del self.ball
                self.ball=Ball(self)

    


if __name__=="__main__":
    game = Game()
    arcade.run()
