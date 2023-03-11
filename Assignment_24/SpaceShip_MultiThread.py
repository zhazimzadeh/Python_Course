import random
from timeit import default_timer as timer
import time
import threading
import arcade

    
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=700,title="Interstellar game 2023")
        arcade.set_background_color(arcade.color.DARK_CERULEAN)
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.explosionSound=arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.bulletSound=arcade.sound.load_sound(":resources:sounds/hurt3.wav")
        self.me=Spaceship(self.width)
        # self.enemy=Enemy(self.width,self.height)
        self.enemy_list=[]
        self.heart_list=[]
        self.flgStart=1
        self.flgGameOver=0
        x=10
        for i in range(0,3):
            heart=Heart(x)
            self.heart_list.append(heart)
            x+=30

        self.startTime=timer()
        self.endTime=timer()
        self.score=0
        self.scoreOld=0
        self.enemySpeed=2
        self.my_thread=threading.Thread(target=self.create_enemy)
        self.my_thread.start()

        


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        for heart in self.heart_list:
            heart.draw()

        for enemy in self.enemy_list:
            enemy.draw()
        
        for bullet in self.me.bullet_list:
            bullet.draw()

        arcade.draw_text(self.score,self.width-50,10,arcade.color.YELLOW,20)

        if(len(self.heart_list)==0):
            arcade.draw_rectangle_filled(0,0,self.width*2,self.height*2,arcade.color.BLACK)
            # arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over!",self.width//2-50,self.height//2,arcade.color.WHITE,25)          

            a=timer()
            if(int(timer()-a)>5):
                self.enemy_list.clear()
                self.me.bullet_list.clear()
                del self.me  
                exit(0)

        arcade.finish_render()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.LEFT:
            self.me.change_x=-1           
        elif symbol==arcade.key.RIGHT:
            self.me.change_x=1    
        elif symbol==arcade.key.DOWN:
            self.me.change_x=0   
        elif symbol==arcade.key.SPACE:
            self.me.fire()


    def create_enemy(self):
        while True:
            self.new_enemy=Enemy(self.width,self.height,self.enemySpeed)
            self.enemy_list.append(self.new_enemy)
            time.sleep(3)
            
    def on_update(self, delta_time: float):
        
        # self.endTime=timer()
        # if(self.flgStart):
        #     self.flgStart=0
        #     self.startTime=timer()      
        #     self.new_enemy=Enemy(self.width,self.height,self.enemySpeed)
        #     self.enemy_list.append(self.new_enemy)

        # elif int(timer()-self.startTime)>=3:  
        #     self.startTime=timer()      
        #     self.new_enemy=Enemy(self.width,self.height,self.enemySpeed)
        #     self.enemy_list.append(self.new_enemy)



        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me,enemy):
                self.enemy_list.remove(enemy)
                for heart in self.heart_list:
                    self.heart_list.remove(heart)
                    break
                arcade.sound.play_sound(self.explosionSound)

                

        for bullet in self.me.bullet_list:
            for enemy in self.enemy_list:
                if arcade.check_for_collision(bullet,enemy):
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    self.score+=1
                    arcade.sound.play_sound(self.bulletSound)

        self.me.move()
        if(self.score-self.scoreOld==10):
            self.enemySpeed+=1           
            self.scoreOld=self.score

        for enemy in self.enemy_list:
            enemy.move()
            if(enemy.center_y<0):
                self.enemy_list.remove(enemy)
                for heart in self.heart_list:
                    self.heart_list.remove(heart)
                    break


        for bullet in self.me.bullet_list:
            bullet.move()
            if(bullet.center_y>self.height):
                self.me.bullet_list.remove(bullet)



class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed=3
        self.center_x=host.center_x
        self.center_y=host.center_y
        self.change_x=0
        self.change_y=-1

    def move(self):
        self.center_y +=self.speed

class Spaceship(arcade.Sprite):
    def __init__(self,w) :
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x=w//2
        self.center_y=80
        self.width=48
        self.height=48
        self.speed=4
        self.change_x=0
        self.change_y=0
        self.game_width=w
        self.bullet_list=[]

    def move(self):
        if(self.change_x==-1):
            if(self.center_x>0):
                self.center_x -=self.speed
        elif(self.change_x==1):
            if(self.center_x<self.game_width):
                self.center_x +=self.speed

    def fire(self):
        new_bullet=Bullet(self)
        self.bullet_list.append(new_bullet)

class Heart(arcade.Sprite):
    def __init__(self,x):
        super().__init__("Assignment_24\heart.png")
        self.center_x=x
        self. center_y=10
        self.width=20
        self.height=20 

class Enemy(arcade.Sprite):
    def __init__(self,w,h,speed):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x=random.randint(0,w)
        self.center_y=h+24
        self.angle=180
        self.width=48
        self.height=48
        self.speed=speed

    def move(self):
        self.center_y-=self.speed


        
        


window=Game()
arcade.run()