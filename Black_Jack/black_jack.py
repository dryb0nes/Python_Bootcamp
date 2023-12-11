
import random
import os


player_cards = []
dealer_cards = []

def clear_screen():
    """This will clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear' )

def deal_cards(dealing_to):
    # Ten_Card draw = 31% chance, 2-9 draw = 69% chance
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    dealing_to.append(random.choice(cards))

def player_hit():
    clear_screen()
    player_cards_print = f"Your Cards {' '.join(str(num) for num in player_cards)} \n"
    print(f"Dealer has {dealer_cards[0]} {dealer_cards[1]} \n")
    print(player_cards_print)
    player_hit_input = input("Would you like to Hit 'h' or Stand 's'?  ").lower()
    if player_hit_input == 'h':
        deal_cards(player_cards)
        if sum(player_cards) < 21:
            player_hit()
        elif sum(player_cards) > 21:
            print(player_cards_print)
            print("You Bust!")
            exit()
    elif player_hit_input == 's':
        print("Player stands.\n")
    else:
        print("Invalid input. Please enter 'h' or 's'.")
        player_hit()  # Recursive call for invalid input

def dealer_hit():
    while sum(dealer_cards) < 17:
        deal_cards(dealer_cards)
    if sum(dealer_cards) > 21:
        print(f"Dealer busts with {sum(dealer_cards)} \n\nYou win!")
        exit()
    

play = input("Would you like to play Blackjack? 'y' or 'n' ").lower()

dealer_cards_print = f"Dealer has  {' '.join(str(num) for num in dealer_cards)}"
if play == 'y':
    while len(player_cards) < 2:
        deal_cards(player_cards)
    while len(dealer_cards) < 2:
        deal_cards(dealer_cards)
    dealer_cards_print = f"Dealer has  {' '.join(str(num) for num in dealer_cards)}"
    print(dealer_cards_print)
    player_hit()
    dealer_hit()
else:
    exit()

dealer_card_total = sum(dealer_cards)
player_card_total = sum(player_cards)
if dealer_card_total == player_card_total:
    print("Push!")
elif dealer_card_total > player_card_total:
    print(f"Dealer wins with {dealer_card_total}!")
elif dealer_card_total >= 17 and dealer_card_total < player_card_total:
    print(f"You win with {player_card_total}")


#testing


