# import random
import arcade
from br_Rocket import br_Rocket
from br_Heart import br_Heart
from br_Ball import br_Ball
from br_Element import br_Element




rocket_pic="Python_Course\Assignment_16\paddleblue.png"  
ball_pic="Python_Course\Assignment_16\Tennis-ball.png"
blue_pic="Python_Course\Assignment_16\element_blue.png"
green_pic="Python_Course\Assignment_16\element_green.png"
red_pic="Python_Course\Assignment_16\element_red.png"
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=700,title="Breakout 2023")
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.score=0
        self.heart_list=[]
        self.element_list=[]
        self.flgGameOver=0
        self.me= br_Rocket(self.width,rocket_pic)
        self.ball=br_Ball(self.me,ball_pic)
        x=30
        for i in range(0,3):
            heart=br_Heart(x,rocket_pic)
            self.heart_list.append(heart)
            x+=50
        y=self.height-20
        for j in range (0,4):
            x=40
            for i in range(0,14):
                element=br_Element(x,y,blue_pic)
                self.element_list.append(element)
                x+=70

            x=40
            y-=30
            for i in range(0,14):
                element=br_Element(x,y,red_pic)
                self.element_list.append(element)
                x+=70

            y-=30
            x=40
            for i in range(0,14):
                element=br_Element(x,y,green_pic)
                self.element_list.append(element)
                x+=70
            y-=30



        


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        self.ball.draw()
        for heart in self.heart_list:
            heart.draw()
        for element in self.element_list:
            element.draw()

        arcade.draw_text(self.score,self.width-50,10,arcade.color.YELLOW,20)

        if(len(self.heart_list)==0) :
            arcade.draw_rectangle_filled(0,0,self.width*2,self.height*2,arcade.color.BLACK)
            arcade.draw_text("Game Over!",self.width//2-50,self.height//2,arcade.color.WHITE,25)          
       
        if(len(self.element_list)==0):
            arcade.draw_rectangle_filled(0,0,self.width*2,self.height*2,arcade.color.CYAN)
            arcade.draw_text("You Win!",self.width//2-50,self.height//2,arcade.color.YELLOW,25)          


        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol==arcade.key.LEFT:
            self.me.change_x=-1           
        elif symbol==arcade.key.RIGHT:
            self.me.change_x=1     



    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # if self.me.width <x <self.width-10:
             self.me.center_x=x

    def on_update(self, delta_time: float):

        for element in self.element_list:
                if arcade.check_for_collision(self.ball,element):
                    self.element_list.remove(element)
                    self.score+=1
                    self.ball.change_y*=-1
                    break

        if self.ball.center_x <20 or self.ball.center_x>self.width-20:
                self.ball.change_x *=-1

        if arcade.check_for_collision(self.me,self.ball) :
                self.ball.change_y*=-1 
               

        if self.ball.center_y <0:
            self.heart_list.pop()
            self.score-=1
            del self.ball
            self.ball=br_Ball(self.me,ball_pic)
            

        self.me.move()
        self.ball.move()







        
      



        
        


window=Game()
arcade.run()