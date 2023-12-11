# Calulator
# It should take a number as an input
# then prompt the user to pick + - * / operation
# then prompt for a second number
# then return the result and store the result for future operations
# it should then prompt the user if they want to do another operation and if that operation will be a continuance of the current result or a new operation
# All numbers should be in a single decimal float


import os
import time

def clear_screen():
    """ This function will clear the terminal screen when called."""
    os.system('cls' if os.name == 'nt' else 'clear')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operation_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}   

history = []
finished = False
while not finished:
    try:
        first_number = float(input("What is the first number: "))
        print('''
            +   plus
            -   subtract
            *   multiply
            /   divide
        ''')
        operation = input("Plesae select an operation: ")

        # Check if the operation is valid
        if operation not in operation_dictionary:
            print("Invalid operation. Please choose a valid operation.")
            time.sleep(1)
            clear_screen()
            continue

        second_number = float(input("What is the second number: "))
        result = operation_dictionary[operation](first_number, second_number)

        if result is not None:
            print(f"{first_number} {operation} {second_number} = {result}")
            history.append(result)
        
        another_operation = input("Do you want to perform another operation? ").lower()
        if another_operation != 'yes':
            finished = True
        
    except ValueError:
        print("Please enter valid numbers.")
        time.sleep(1)
        clear_screen()