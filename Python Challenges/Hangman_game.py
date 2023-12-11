# Section 1
# TODO - 1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO - 2 - Ask the user to guess a letter and assin their answer to a variable called guess. Make guess lowercase.

# TODO - 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Section 2
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#Secion 3
# TODO - 1 - Use a while loop to let the user guess again. The Loop should only stop once the user has guessed all the letters in the chose_word and 'display' has no more blanks("_"). THen you can tell the user they've won.

# Section 4
# TODO - 1 - create a variable called lives to live and set it to 6
# TODO - 2 - If guess is not a letter in the chosen_word, then reduce "lives" by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."
import random
import os

hangman_pics = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['horse', 'door', 'song', 'trip', 'backbone', 'bomb', 'round', 'treasure', 'garbage', 'park', 'pirate', 'ski', 'state', 'whistle', 'palace', 'baseball', 'coal', 'queen', 'dominoes', 'photograph', 'computer', 'hockey', 'aircraft', 'hot', 'dog', 'salt', 'and', 'pepper', 'key', 'iPad', 'whisk', 'frog', 'lawnmower', 'mattress', 'pinwheel', 'cake', 'circus', 'battery', 'mailman', 'cowboy', 'password', 'bicycle', 'skate', 'electricity', 'lightsaber', 'thief', 'teapot', 'deep', 'spring', 'nature', 'shallow', 'toast', 'outside', 'America', 'roller', 'blading', 'gingerbread', 'man', 'bowtie', 'half', 'spare', 'wax', 'light', 'bulb', 'platypus', 'music']
chosen_word = random.choice(word_list).lower()
display = ["_"] * len(chosen_word)
previous_guesses = []
lives_left = 6
current_hangman = hangman_pics[lives_left]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

while "_" in display and lives_left > 0:

    # prints a list of previously guessed letters
    print(f"Previous Guesses: {' '.join(previous_guesses)}\n")
    print(f"The Word is: {' '.join(display)}")

    current_hangman = hangman_pics[lives_left]
    print(f"{current_hangman}\n")
    
    guess = input("Please type a letter and hit 'Enter': ").lower()
    print("")
    # enumerate is used here to keep track of both the current letter we are iterating over as well as its index position to be used later when we replace the "_" in display with the current letter.
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            clear_screen()
            print("Correct!\n")
            display[index] = letter

    if guess not in chosen_word and lives_left > 0:
        clear_screen()
        print("Incorrect!\n")
        lives_left -= 1
    
    previous_guesses.append(guess) # adds previously guessed letters to the list so they can be displayed.
    
if lives_left == 0:
    clear_screen()
    print(f"The word was {chosen_word}\n")
    print(''' 
 __   __                            _                                _    
 \ \ / /   ___    _  _      o O O  | |      ___     ___     ___     | |   
  \ V /   / _ \  | +| |    o       | |__   / _ \   (_-<    / -_)    |_|   
  _|_|_   \___/   \_,_|   TS__[O]  |____|  \___/   /__/_   \___|   _(_)_  
_| """ |_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_| """ | 
"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
          
''')
    
elif "_" not in display:
    clear_screen()
    print(f"The word was {chosen_word}")
    print('''                                                                                                                                
YYYYYYY       YYYYYYY                                     WWWWWWWW                           WWWWWWWW iiii                    !!! 
Y:::::Y       Y:::::Y                                     W::::::W                           W::::::Wi::::i                  !!:!!
Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W iiii                   !:::!
Y::::::Y     Y::::::Y                                     W::::::W                           W::::::W                        !:::!
YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu        W:::::W           WWWWW           W:::::Wiiiiiiinnnn  nnnnnnnn    !:::!
   Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         W:::::W         W:::::W         W:::::W i:::::in:::nn::::::::nn  !:::!
    Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u          W:::::W       W:::::::W       W:::::W   i::::in::::::::::::::nn !:::!
     Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u           W:::::W     W:::::::::W     W:::::W    i::::inn:::::::::::::::n!:::!
      Y:::::::Y   o::::o     o::::ou::::u    u::::u            W:::::W   W:::::W:::::W   W:::::W     i::::i  n:::::nnnn:::::n!:::!
       Y:::::Y    o::::o     o::::ou::::u    u::::u             W:::::W W:::::W W:::::W W:::::W      i::::i  n::::n    n::::n!:::!
       Y:::::Y    o::::o     o::::ou::::u    u::::u              W:::::W:::::W   W:::::W:::::W       i::::i  n::::n    n::::n!!:!!
       Y:::::Y    o::::o     o::::ou:::::uuuu:::::u               W:::::::::W     W:::::::::W        i::::i  n::::n    n::::n !!! 
       Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu              W:::::::W       W:::::::W        i::::::i n::::n    n::::n     
    YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u               W:::::W         W:::::W         i::::::i n::::n    n::::n !!! 
    Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u                W:::W           W:::W          i::::::i n::::n    n::::n!!:!!
    YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu                 WWW             WWW           iiiiiiii nnnnnn    nnnnnn !!!                                                                                                                     
''')

