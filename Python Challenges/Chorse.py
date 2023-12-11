chore_prices = {
    "bedroom": 1,
    "living_area": .5,
    "bathroom": 5,
    "brushing_teeth": .25,
    "unload_dishwasher": 1,
    "vacuume": 2,
    "mopping": 2,
    "laundry": 2,    
}

total = 0

for chore_value in chore_prices.values():
    total += chore_value

print(total)