import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

names_index = len(names) - 1

random_index = random.randint(0, names_index)

person_to_pay = names[random_index]

print(f"{person_to_pay} is going to buy the meal today!")
