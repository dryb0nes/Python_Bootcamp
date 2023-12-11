# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# Write your code below this line 👇

import math

def prime_checker(input_number):
    # this for loop interates through a range starting at 2, up to the square root of the input number.
    # the math.isqrt() function is used as it improves the efficiany slightly by creating a smaller pool of numbers to test.
    # the .isqrt() is used specifically because it automatically rounds down to the nearest whole integer to the square root of the input number. 
    # the "+ 1" is used to include the square of the number in the testing.
    for number in range(2, math.isqrt(input_number) + 1):
        if input_number % number == 0:
            print("It's not a prime number.")
            # this break statement stops the loop once we have found an even divisor again improving the program efficiancy.
            break
    # this else statement is used in the "for" loop and will trigger if hen the loop exhausts its iterable (in this case, when the loop completes without encountering a break)
    else:
        print("It's a prime number.")
        
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(input_number=n)