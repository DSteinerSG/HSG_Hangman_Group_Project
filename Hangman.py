#####

# Python version of the Hangman Guessing Game
# by Luca Gmuer, Dejan Sajlovic, Daniel Steiner

#####


############ Preparing the environment ############

# importing libraries
import random
import os
import subprocess


# opening a list with common english words
with open('words.txt', 'r') as file:
    words = file.read().splitlines()


# init variable for consecutive rounds
repeat = 1

# dividing print statements
def cell_divider():
    print("\n"+"#"*80+"\n")

# difficulty levels and name possibilities
diff_dic = {'E': 'EASY', 'M': 'MEDIUM', 'H': 'HARD'}
names_possible = list("abcdefghijklmnopqrstuvwxyzäöü ")


# Asking the player for a valid name and greeting them
while True:

    name = input('Please enter your name: ')
    if set(name.lower()).issubset(set(names_possible)):
        print('\nHello' + ' ' + name + ',' + ' ' + "let's play Hangman!")
        break
    else:
        print("Please input a valid name.")

# Hangman rules explanation
tutorial = "\n\n" + "#"*80 + "\n" + "Hello" + " " + name + "," + " " + """welcome to our Hangman game!\n
Hangman is a game where you have to guess a secret word by suggesting letters.
The only thing you know in advance is the number of letters of the word you are looking for.
This is represented by the number of underscores.
If you guess a correct letter, the underscore will be 
replaced by the correct letter at the appropriate position. If your suggested letter is wrong and not 
present in the hidden word, this counts as a miss.

This game can be played both casually for a single round and competitively, where you have to win 3 rounds on the same 
level of difficulty to win a unique certificate. There are three different levels of difficulty, 
differing by the number of allowed misses. In the easy level you have a total of 10 misses, 
in the medium level 7 and in the hard level 5. If you manage to correctly guess the word with fewer misses, 
you win. Otherwise you lose.\nGood luck!""" + "\n" + "#"*80



############ Defining functions for every part of the game ############

##### choosing the game mode #####
def mode_setter():

    # looping for tutorial and input validation purposes
    while True:

        game_mode = input("\nChoose a game mode: Single-round (S), Competition (C) or Tutorial (T)").upper()

        if game_mode == 'T':  # Shows the rules
            print(tutorial, "\n")

        elif game_mode == 'S':  # Only one word will be presented
            comp = 0
            num_games = 1
            break

        elif game_mode == 'C':  # three words with chance to receive certificate
            comp = 1
            num_games = 3
            break

        else:  # checking for wrong input
            print("\n\n\nPlease enter a valid input.\n\n\n")

    return comp, num_games


##### choosing the difficulty #####
def choose_difficulty():

    # looping for input validation
    while True:

        # ask the player to choose the level of difficulty (easy, medium or hard)
        difficulty = input('\nPlease choose the level of difficulty: Easy (E), Medium (M) or Hard (H) ').upper()

        # if the input is correct continue with the game
        if difficulty in ('E', 'M', 'H'):
            break

        # if the input is wrong, ask the player to enter a valid level of difficulty
        else:
            print('Wrong input. Please enter a valid level of difficulty.')

    return difficulty


##### defining one round of Hangman #####
def game_round():

    # allowing the function to manipulate global variables
    global max_number_of_misses
    global num_games
    global round_wins

    # randomly choosing a hidden word
    word = random.choice(words)

    # difficulty dependent number of wrong guesses
    if difficulty == 'E':
        max_number_of_misses = 10

    elif difficulty == 'M':
        max_number_of_misses = 7

    elif difficulty == 'H':
        max_number_of_misses = 5

    # what the player can see after every letter
    visible = ["_" for n in range(len(word))]

    # win condition:
    won = 0

    # counting the wrong_guesses:
    wrong_guesses = []

    # lists of all possible letters and letters not yet tried:
    letters_possible = list("abcdefghijklmnopqrstuvwxyz")
    letters = list("abcdefghijklmnopqrstuvwxyz")

    # looping for every input until the round is either won or lost
    while len(wrong_guesses) < max_number_of_misses:

        # divider
        cell_divider()

        # checking for won round
        if "_" not in visible:
            won = 1
            break

        print("\n")
        print(*visible)
        print(f"\n\nWrong guesses: {*wrong_guesses,}   {max_number_of_misses - len(wrong_guesses)} remaining.\n\n")


        # checking if guess is valid
        guess = input("Please enter a letter to try: ").lower()

        if guess not in letters_possible:
            print("\nPlease enter a valid letter.")

        elif guess not in letters:
            print("\nYou have already guessed this letter.")

        else:
            # prevent guessing the same letter twice
            letters.remove(guess)

            # showing correct letters
            for char in range(len(word)):

                if guess == word[char]:
                    visible[char] = guess

            # updating list of wrong guesses
            if guess not in word:
                wrong_guesses.append(guess)


    if comp == 0:  # check for Single-Round game mode

        num_games = 0

        if won == 1:
            print("You won the game!")

        else:
            print("\nYou lost the game.")

        # print the correct word
        print("\nThe correct word was:", word)


    else:  # competition mode

        if won == 1:

            # Print the correct word
            print("You won the round!\n")
            print("The correct word was:", word)

            # adjust number of rounds:
            num_games -= 1
            round_wins += 1

            if num_games > 0:
                print("\nNext round!")

        else:

            print("\nYou lost the game.")
            print("\nThe correct word was:", word)


            # adjust number of games:
            num_games = 0
            round_wins = 0


##### repeating the rounds for one total game #####
def game_flow():
    while num_games > 0:
        game_round()


##### printing a certificate to a txt file #####

def open_certificate(certificate):
    # differentiating the different commands for each operating system
    # to achieve this, we use if statements
    
    # Windows
    if os.name == 'nt':  
        with open(f'Hangman_certificate_{diff_dic[difficulty]}.txt', 'w') as file:
            file.write(certificate)
        subprocess.run(['start', f'Hangman_certificate_{diff_dic[difficulty]}.txt'], shell=True)
        
   # macOS or Linux
    elif os.name == 'posix':  
        with open(f'Hangman_certificate_{diff_dic[difficulty]}.txt', 'w') as file:
            file.write(certificate)
        subprocess.run(['open', f'Hangman_certificate_{diff_dic[difficulty]}.txt'])
        
    # if neither the Windows nor the macOS/Linux command is applicable we need to print an error message
    else:
        print("Unsupported operating system: cannot print the certificate.")


##### creating the template for the certificate #####
# passing in variables to individualise the certificate

certificate_template = """

_____________________________________________________________________________________________________

**************************************| Congratulations |********************************************

_____________________________________________________________________________________________________


You, {name}, have successfully completed our hangman game on the {diff} difficulty!

We hope you will play again soon!

_____________________________________________________________________________________________________

"""



############ starting the actual game ############

while repeat == 1:

    # comp or casual
    comp, num_games = mode_setter()

    # difficulty
    difficulty = choose_difficulty()

    # reset round count
    round_wins = 0

    # start the game
    game_flow()

    # generate and open the certificate if the player meets the requirements
    if comp == 1 and round_wins == 3:

        certificate = certificate_template.format(name=name, diff=diff_dic[difficulty])
        open_certificate(certificate)


    # looping for input validation
    while True:
        
        # ask the player whether he/she wants to play again
        play_again = input('\nDo you want to play again? Input YES or NO: ').upper()
        
        # if YES, start the game again
        if play_again == 'NO':
            repeat = 0
            break
        
        # if NO, end the game and thank the player for playing Hangman
        elif play_again == 'YES':
            cell_divider()
            break
        
        # if incorrect input, prompt the player to enter a correct input
        else:
            print("\nPlease only input YES or NO.")




print("\nThank you for playing Hangman!")
