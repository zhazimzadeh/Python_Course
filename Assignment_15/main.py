from timeit import default_timer as timer
import arcade

from apple import Apple
from snake import Snake

apple_pic="apple.png"
shit_pic="shit.png"
pear_pic="pear.png"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=500,title="My Snake")
        arcade.set_background_color(arcade.color.KHAKI)

        self.apple=Apple(self,apple_pic)
        self.shit=Apple(self,shit_pic)
        self.pear=Apple(self,pear_pic)
        self.snake=Snake(self,0)
        self.gameOver=0
        self.first=1


    def on_draw(self):
        arcade.start_render()
        if self.gameOver==1:
            arcade.draw_rectangle_filled(0,0,self.width*2,self.height*2,arcade.color.BLACK)
            # arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over!",self.width//2-70,self.height//2,arcade.color.WHITE,25)          

            a=timer()
            if(int(timer()-a)>10):
                del self.apple
                del self.pear 
                del self.shit
                del self.snake 
                exit(0)

        if self.gameOver==0:
            self.apple.draw()
            self.shit.draw()
            self.pear.draw()
            self.snake.draw()
            arcade.draw_text(self.snake.score,self.width-50,10,arcade.color.YELLOW,20)
        
        arcade.finish_render()


    def on_update(self, delta_time: float):
        if(self.gameOver==0):
            self.snake.move()

            if arcade.check_for_collision(self.snake,self.apple):
                self.snake.eat(self.apple,1)
                self.apple=Apple(self,apple_pic)
                self.first=0
            
            if arcade.check_for_collision(self.snake,self.shit):
                self.snake.eat(self.shit,-1)
                self.shit=Apple(self,shit_pic)
                self.first=0

            if arcade.check_for_collision(self.snake,self.pear):
                self.snake.eat(self.pear,2)
                self.pear=Apple(self,pear_pic)
                self.first=0

            if self.first==0:
                if self.snake.score<=0:
                    self.gameOver=1

            if self.snake.center_x< 0:
                self.gameOver=1

            elif self.snake.center_x> self.width:
                self.gameOver=1

            elif self.snake.center_y <0:
                self.gameOver=1

            elif self.snake.center_y > self.height:
                self.gameOver=1


            # i=0
            # if len(self.snake.body)>60:
            #     for i in range(0,len(self.snake.body)):
            #         if i>60:
            #             if arcade.check_for_collision(self.snake.body[0],self.snake.body[i]):
            #         # if i>60:
            #             # if self.snake.center_x==part['x'] and self.snake.center_y==part['y']:
            #             #
            #                  self.gameOver=1
            #             #     break
            #         # i+=1


    



    

        


    def on_key_release(self, symbol: int, modifiers: int):
        if arcade.key.UP==symbol:
            self.snake.change_x=0
            self.snake.change_y=1
            # print(symbol)
        elif arcade.key.DOWN==symbol:
            self.snake.change_x=0
            self.snake.change_y=-1
            # print(symbol)
        elif arcade.key.LEFT==symbol:
            self.snake.change_x=-1
            self.snake.change_y=0
            # print(symbol)
        elif arcade.key.RIGHT==symbol:
            self.snake.change_x=1
            self.snake.change_y=0
            # print(symbol)

 
        # for part in self.snake.body:
        #         if self.snake.center_x==part['x'] and self.snake.center_y==part['y']:
        #             self.gameOver=1
        #             break







if __name__=="__main__":
    game = Game()
    arcade.run()
