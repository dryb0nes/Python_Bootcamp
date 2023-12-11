import turtle
from turtle import Turtle

movement = {}
tim = Turtle()

# determines degrees for each shape and addes the number of sides and the degrees to turn for that shape to a dictionary called "degrees"
for i in range(3, 11):
    degrees = round(360 / i)
    movement[i] = degrees

# tells turtle to start from home move forward 100 paces then chane dirction a specified number of degrees based on the shape to be drawn.
for sides, degrees in movement.items():
    sides_completed = 0
    while sides_completed < sides: # loop back to moving forward again. Complete this until tim gets back to home coordinates(0,0)
        tim.forward(100)
        tim.right(degrees) # turns tim right a defined number of degrees needed to drap the specified shape based on the number of sides
        sides_completed += 1 # increment sides_completed so that by the time we are back at the home position we should have drawn all sides and we will break out of the loop
    tim.home() # repositions tim back to starting position and heading so he starts from the same position after each interation

turtle.mainloop()


# Solution
# ########### Challenge 3 - Draw Shapes ########

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)