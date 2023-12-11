import math
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

test_time = 1

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    else:
        print(f"the count is {count}, and the count_sec is {count_sec}.")
    time.sleep(1)
    if count > 0:
        count_down(count - 1)
        
reps = 3

while reps < 4:
    print(reps)
    print("while loop started")
    count_down(test_time * 60) # work time test
    print("short breka start")
    count_down(0.5 * 60) # short break test
    reps += 1
    clear_screen()
else:
    print("else started")
    count_down(10 * 60)
    count_down(20 * 60)