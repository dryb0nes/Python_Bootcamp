import turtle
from turtle import Turtle
import random


tim = Turtle()
tim.shape("circle")
tim.width(20)
screen = turtle.Screen()
def move():
    tim.forward(1)


screen.listen()
screen.onkeypress(move, "w")


turtle.mainloop()