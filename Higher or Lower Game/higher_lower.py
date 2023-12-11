
import random
import os
import time
from art import title_graphic
from game_data import name_list


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# create a function that "shuffles" list of dictionaries and just pop[0] from the list to get new name.
def pull_names():
    random.shuffle(name_list)
    names_list= []
    for i in range(2):
        names_list.append(name_list.pop(0))
    return names_list

def compare(celebrity_list):
    if celebrity_list[0]['followers'] > celebrity_list[1]['followers']:
        return celebrity_list[0]
    else:
        return celebrity_list[1]

def celebrity_info(celebrity_list):
    return f"{celebrity_list['name']}\n{celebrity_list['description']} from {celebrity_list['country']}."

def check_guess(user_guess, celebrity_list):
    if user_guess == 'a':
        user_guess = celebrity_list[0]
    elif user_guess == 'b':
        user_guess = celebrity_list[1]
    most_followers = compare(celebrity_list)
    if most_followers['name'] == user_guess['name']:
        # celebrity_list.pop(most_followers)
        return "Correct!"
    else:
        return "Incorrect! You Lose!"

def space():
    print()

def game(correct_counter):
    print(title_graphic)
    celebrity_list = pull_names()
    print(f"Correct Guesses: {correct_counter}")
    space()
    print(celebrity_info(celebrity_list[0]))
    space()
    print("************* vs *************")
    space()
    print(celebrity_info(celebrity_list[1]))
    space()
    user_guess = input(f"Who has more followers? 'a' for {celebrity_list[0]['name']} or 'b' for {celebrity_list[1]['name']}: ").lower()
    space()
    print(check_guess(user_guess, celebrity_list))
    time.sleep(1)
    if check_guess(user_guess, celebrity_list) == 'Correct!':
        correct_counter += 1
        clear_screen()
        game(correct_counter)
    return correct_counter


correct_counter = 0
game(correct_counter)

while input("Would you like to play again? 'y' or 'n': ") == "y":
    clear_screen()
    game(correct_counter)
# Testing
# print(pull_name())