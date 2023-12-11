import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Hunt!")
print("Your mission is to find the treasure.\n\n") 

#Write your code below this line 👇
def start():
    game_continue = input("Continue? Yes or No \n").lower()

    if game_continue == "yes":
        print('''Once upon a time, in a vibrant and magical land, lived a curious and brave kid named Max. Max loved exploring the mysterious Forest of Wonders, where tales of a hidden treasure had been whispered through the leaves. \n\n''')
        time.sleep(5)

        print('''With an old map, Max set off on the adventure of a lifetime. The map revealed that the treasure was hidden in different locations marked by special words. \n\n''')

    return game_continue == "yes"

def forest():
    time.sleep(2)
    print('''Max's first challenge was to find the "tree" where the wise owl, Ollie, resided. Ollie would give a clue leading to the next sight word location. \n''')
    time.sleep(2)
    direction = input("Head East or West through the forest? \n")
    
    if direction == "west":
        print('''\nMax wandered through the enchanted forest until he spotted a majestic oak tree with Ollie perched on a branch. \n''')
        time.sleep(2)
    else:
        print("You traveled outside of the foreset! Game over! \n")
        time.sleep(2)
        return input("Restart at the forest entrance? Yes or No \n").lower() == "yes"

    print('''Ollie hooted, "Great adventurer, your first clue lies where the river'flows.' Follow the sparkly stones, and you'll uncover the next word. \n''')
    time.sleep(2)
    river_direction = input("Will you head north or south along the river? North or South? \n").lower()

    if river_direction == "north":
        time.sleep(2)
        print('''\nAfter traveling North for quite a while, Max saw a large group of flowers and butterflies a small ways away from a odd looking bridge. Max walked over to the butterflies and among the flowers found the word "bridge" spelled out in colorful stones. The next clue was pointing towards the "bridge", which appeared to be guarded by some mischievous looking fairies.''')
            
    else:
        time.sleep(2)
        print("\nYou head south, but soon after a TROLL rumbles out of the forest! \n\n")
        fight_troll = input("Will you fight the troll or will you flee back north? Fight or Flee? \n").lower()

        if fight_troll == "fight":
            print('''Max takes a deep breath and lunges at the troll! Right as Max is about to strike, the troll whips a large club around smashing it against Max! Max flies backwards slamming into a tree, soon becoming unconcious.''')
            time.sleep(.6)
            print('''Max has been knocked out. Game Over. \n\n''')
            return input("Restart at the forest entrance? Yes or No \n").lower() == "yes"
        else:
            print('''\nMax raced back North along the river away from the massive troll. \n''')
            time.sleep(2)

            print('''After traveling North for quite a while, Max saw a large group of flowers and butterflies a small ways away from a odd looking bridge. Max walked over to the butterflies and among the flowers found the word "bridge" spelled out in colorful stones. The next clue was pointing towards the "bridge", which appeared to be guarded by some mischievous looking fairies.''')

    return True

def bridge():
    time.sleep(3)
    print('''\nAs Max approached the bridge, the fairies all turned to him and giggled saying, "To continue young adventurer, answer our riddle: \n''')
    print("What has keys but can't open locks?  \n")
    attempts = 3
    while attempts > 0:
        player_answer = input("Your answer: ").lower()
        if player_answer == "piano":
            print('''\nThe fairies cheered and and allowed Max to pass over the bridge continuing along the path!\n''')
            break
        else:
            attempts -= 1
            print(f'''Incorrect! You have {attempts} {'attempts' if attempts > 1 else 'attempt'} remaining.\n''')

    if attempts == 0:
        print("Thank you adventurer for playing!")
        return input("Do you want to restart the riddle? Yes or No").lower() == "yes"

    print('''\nAlong the path you find a sword with a hidden note attached.''') 
    time.sleep(2)
    
    cave_riddle = input("On the note is a riddle. I'm dark and deep, a secret I keep. Enter my mouth but not through teeth. I'm not alive, yet I can grow. What am I? \n")

    if cave_riddle == "cave":
        print('''Correct! You run deeper into the forest now searching for a hidden cave. After hours of searching you finally find the entrance at the base of a mountain!''')
    
while start():
    while forest():
        while bridge():
            pass

print("Thank you adventurer for playing!")