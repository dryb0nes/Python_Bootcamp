
import random
import os
from art import guess_the_number

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def compare(guess, current_number):
        if guess == current_number:
            return "Correct! You win!"
        elif guess > current_number:
            return "Too High!\n"
        elif guess < current_number:
            return "Too Low!\n"

def make_a_guess(n_to_guess, n_of_guesses):
    while n_of_guesses >= 1:
        print(f"Current Guesses Left: {n_of_guesses}")
        current_user_guess = int(input("Make a guess: "))
        check_guess = compare(current_user_guess, n_to_guess)
        if check_guess == "Correct! You win!":
                print(check_guess)
                break
        else: 
            n_of_guesses -= 1
            print(check_guess)

    else:
        print(f"You lose! The number was {n_to_guess}.\n")

def play_game():
    print(guess_the_number)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    n_to_guess = random.randint(1, 100)
    n_of_guesses = 0
    hard_mode = 5
    easy_mode = 10
    while n_of_guesses == 0:
        game_difficulty = input("Choose a difficulty: 'easy' or 'hard': ").lower()
        if game_difficulty == 'easy':
            n_of_guesses = easy_mode
        elif game_difficulty == 'hard':
            n_of_guesses = hard_mode
        else:
            print("Invalid input. Please select 'easy' or 'hard'.")

    print()
    make_a_guess(n_to_guess, n_of_guesses)
    
play_game()
while input("Do you want to play again? Type 'y' or 'n': ") == "y":
        clear_screen()
        play_game()