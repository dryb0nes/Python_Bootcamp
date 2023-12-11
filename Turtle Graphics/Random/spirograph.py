import turtle
from turtle import Turtle
import random

tim = Turtle()
# tim.shape("circle")
# tim.pensize(3)
tim.speed(0)
turtle.colormode(255)
tim.screen.bgcolor('gray')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

# for _ in range(36):
#     tim.circle(100)
#     tim.left(10)
#     tim.color(random_color())



# Solution

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + size_of_gap)
    
draw_spirograph(5)

turtle.mainloop()