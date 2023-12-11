import turtle
from turtle import Turtle
import random

tim = Turtle()
tim.shape("circle")
tim.pensize(10)
tim.speed(0)
turtle.colormode(255)
tim.screen.bgcolor('gray')
headings = [0, 90, 180, 270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

for _ in range(500):
    tim.seth(random.choice(headings))
    tim.forward(25)
    tim.color(random_color())

turtle.mainloop()