import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
             2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
             2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
             2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
             2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10, 10, 11]
    # shuffling the cards
    random.shuffle(cards)
    return cards.pop(0)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Dealer Blackjack! You lose."
    elif player_score == 0:
        return "Winner Winner Chicken Dinner! Blackjack!"
    elif player_score > 21:
        return "You bust!"
    elif dealer_score > 21:
        return "Dealer Bust! You win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You Lose"

def play_game():
    player_cards = []
    dealer_cards = []
    is_game_over = False
    # dealing two cards to the player and dealer
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())


    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"    Your cards: {' '.join(str(card) for card in player_cards)}\n    Current Total: {player_score}")
        print(f"    Dealer's Top Card: {dealer_cards[0]} \n")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_hit = input("Type 'y' to get another card, type 'n' to stand. \n")
            if player_hit == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    print(f"Your final hand: {' '.join(str(card) for card in player_cards)}, final score: {player_score}")
    print(f"Dealer final hand: {' '.join(str(card) for card in dealer_cards)}")
    print(compare(player_score, dealer_score))

play_game()
while input("Do you want to play again? Type 'y' or 'n': ") == "y":
    clear_screen()
    play_game()