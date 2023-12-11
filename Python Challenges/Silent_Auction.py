# The program should take in a users "name" and their "bid" and store that information into a dictionary with a key value pair of "name":"bid". 
# It should then prompt the user if there are more users who need to add their bid.
# If yes then the screen should clear, and the "name" prompt should appear.
# If no then the program should cycle through all bids and announce the winner with their name a how much they bid.

# TODO - Prompt the user to input their name and how much they are bidding. Ensure that the "bid" is stored as an integer not a str.
# TODO - Create a dictionary that that takes in "name":"bid" as the key value pair
# TODO - create a function that takes in the "name" and "bid" and adds that to the dictionary where all user bid information is stored
# TODO - create a function that loops through all bids in the dictionary and returns the highest bidder name and how much they bid
# TODO - print out who the highest bidder was with their name and bid amount

import os

def bid_information(name, bid_amount):
        bidder_information[name] = bid_amount

def highest_bid():
    name = ""
    amount = 0
    for key, value in bidder_information.items():
        if value > amount:
            name = key
            amount = value
    return [name, amount]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

bidder_information = {}

while True:
    bidder_name = input("Please input the bidder's name: ").title()
    bid_amount = int(input("Please input your bid amount: $"))

    bid_information(bidder_name, bid_amount)

    more_users = input("Are there more bids to enter? Type 'yes' or 'no' : ").lower()
    if more_users != "yes":
        break
    else:
         clear_screen()


result = highest_bid()
result_name = result[0]
result_amount = result[1]
print(f"The highest bid was {result_name} with a bid of ${result_amount}!")