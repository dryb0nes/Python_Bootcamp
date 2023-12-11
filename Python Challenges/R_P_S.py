# This is a rock paper scissors game.

import random
import os
def RPS_Game():
    clear_screen()

    Rock = """
    Rock
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---._(___)
                
    """

    Paper = """
    Paper
        _______
    ---'    ____)
            ______)
            _______)
            _______)
    ---.__________)
                
    """

    Scissors = """
    Scissors
        _______
    ---'   ____)
            ______)
        __________)
        (____)
    ---.__(___)
                    
    """
    rock_paper_scissors_list = [Rock, Paper, Scissors]
    computer_choice = rock_paper_scissors_list[random.randint(0, 2)]
    user_choice = input("Choose Rock(R) Paper(P) or Scissors!(S) ").upper()
    player_index = ''

    if user_choice == "R":
        player_index = rock_paper_scissors_list[0]
        print(f"You chose!\n{Rock}")
    elif user_choice == "P":
        player_index = rock_paper_scissors_list[1]
        print(f"You chose!\n{Paper}")
    elif user_choice == "S":
        player_index = rock_paper_scissors_list[2]
        print(f"You chose!\n{Scissors}")

    print("Computer Chooses!\n")
    print(computer_choice) 

    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors

    if player_index == computer_choice:
        print("Draw!")
    elif player_index == Rock and computer_choice == Paper:
        print("Paper beats Rock! You lose!\n\n\n")
    elif player_index == Rock and computer_choice == Scissors:
        print("Rock beats Scissors! You win!\n\n\n")
    elif player_index == Paper and computer_choice == Rock:
        print("Paper beats Rock! You win!\n\n\n")
    elif player_index == Paper and computer_choice == Scissors:
        print("Scissors beats Paper! You lose!\n\n\n")
    elif player_index == Scissors and computer_choice == Rock:
        print("Rock beats Scissors! You lose!\n\n\n")
    elif player_index == Scissors and computer_choice == Paper:
        print("Scissors beats Paper! You win!\n\n\n")

    play_again = input("Would you like to play again? Y or N: ").lower()

    return play_again == "y"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while RPS_Game():
    pass