import turtle
import math


color=["red","orange","Yellow","olive","green","blue","purple","pink"]
p=turtle.Pen()
# p.speed(1)
p.shape("turtle")
p.fillcolor("purple")
turtle.bgcolor("black")
x=0
y=0
Num_Angle = 2
initial_size = 15 
side = 0
c=0
Angle=0
while Angle<180:
  for  c in range(len(color)):
    p.pencolor(color[c])
    x += 8
    initial_size += 8
    Num_Angle += 1
    side = 2 * initial_size * math.sin(math.radians(180/Num_Angle))
    p.penup()
    p.goto((x, y))
    p.pendown()
    interior_angle = (180 * (Num_Angle - 2)) / Num_Angle
    p.setheading(180 - interior_angle//2)
    Angle=180-interior_angle

    for i in range(Num_Angle):
        p.forward(side)
        p.left(Angle)





