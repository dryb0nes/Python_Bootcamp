import turtle
from turtle import Turtle
import random


tim = Turtle()
tim.shape("circle")
tim.width(20)
turtle.colormode(255)
tim.speed('fastest')

colors = [(225, 233, 229), (225, 156, 74), (36, 98, 143), (160, 21, 46), (19, 52, 85), (227, 208, 101), (128, 184, 208), (223, 78, 51), (180, 44, 84), (142, 98, 42), (49, 56, 105), (206, 128, 157), (43, 137, 49), (124, 196, 141), (101, 12, 52), (80, 25, 19), (58, 180, 128)]

# colors should be space 50 apart and the width of the dot should be 20
# the grid should be a 10 x 10

tim.penup()
x = -300
y= -300
tim.setpos(x, y)

for _ in range(10):
    y += 50
    for _ in range(10):
        tim.penup()
        tim.dot(20, random.choice(colors))
        tim.forward(50)
    # need to set coordinates after moving forward 10 times
    tim.setpos(x, y) # will bring tim back to x:0 and move him 50 spaces north to start the next line
    tim.setheading(0) # reset tim back to east
tim.setpos(x, -300)

turtle.mainloop()

















# import colorgram
# import re

# extracted_colors = colorgram.extract('Turtle Graphics\Hirst _Painting\dots.jpg', 20)
# colors_list = []

# for item in extracted_colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     color = (r, g, b)
#     colors_list.append(color)
    


# print(colors_list)

# [(225, 233, 229), (225, 156, 74), (36, 98, 143), (160, 21, 46), (19, 52, 85), (227, 208, 101), (128, 184, 208), (223, 78, 51), (180, 44, 84), (142, 98, 42), (49, 56, 105), (206, 128, 157), (43, 137, 49), (124, 196, 141), (101, 12, 52), (80, 25, 19), (58, 180, 128)]