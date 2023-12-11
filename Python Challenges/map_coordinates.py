line1 = ["A1", "B1", "C1"]
line2 = ["A2", "B2", "C2"]
line3 = ["A3", "B3", "C3"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = ("C3") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# Your job is to write a program that allows you to mark a square on the map using a letter-number system. 

#Remember that nested Lists in Python are accessed from outside to inside. e.g. In the List below:

# list = [['A', 'B, 'C'], 'E', 'F', 'G']

# E is list[1] C is list[0][2]

# splits the input string into a list
position_list = list(position)

# initalizing the x and y coordinate variables for use in our "for" loop
x_coordinate = ""
y_coordinate = ""

for index in position_list:
    if position_list[0] == "A":
        x_coordinate = 0
    elif position_list[0] == "B":
        x_coordinate = 1
    elif position_list[0] == "C":
        x_coordinate = 2

    if position_list[1] == "1":
        y_coordinate = 0
    elif position_list[1] == "2":
        y_coordinate = 1
    elif position_list[1] == "3":
        y_coordinate = 2

# print(position_list)
# print(x_coordinate, y_coordinate)
# print(map[y_coordinate][x_coordinate])

map[y_coordinate][x_coordinate] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")