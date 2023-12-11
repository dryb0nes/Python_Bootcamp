from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os
import time

machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ready_to_make(drink_to_make):
    if machine.is_resource_sufficient(drink_to_make):
        print(f"You Total is: ${drink_to_make.cost}0")
        return money.make_payment(drink_to_make.cost)

while True:
    # User Interaction of selecting a drink
    user_request = input("Please select Espresso, Latte, or Cappuccino: ").lower()

    # turns off the machine for maintenance
    if user_request == 'off':
        break

    # prints a report of th current resources for the machine. 
    elif user_request == 'report':
        machine.report()
        money.report()
    else:
        # checking if drink exists in the menu
        drink_to_make = menu.find_drink(user_request)
        if drink_to_make == None:
            clear_screen()
            print("Please select another item.\n")
            time.sleep(2)
            clear_screen()
        else:
            if ready_to_make(drink_to_make):
                # make the drink
                machine.make_coffee(drink_to_make)
                time.sleep(2)
                clear_screen()
