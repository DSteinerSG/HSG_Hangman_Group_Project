#####

# Python version of the Hangman Guessing Game

#####


############ Preparing the environment ############

# importing libraries
import random



# opening a list with common english words
with open('999 common english words.txt', 'r') as file:
    words = file.read().splitlines()

# TESTING:
words = ["tree", "deer", "star"]


# init variables for consecutive rounds
round_wins = 0
repeat = 1

# Asking the player to enter his/her name and greet him/her
name = input('Please enter your name: ')
print('Hello' + ' ' + name + ',' + ' ' + "let's play Hangman!")

# Hangman rules explanation
tutorial = "Hello" + " " + name + "," + " " + """welcome to the game Hangman. Hangman is a game where you have to 
guess a secret word by suggesting letters. The only thing you know in advance is the number of letters of the word 
you are looking for. This is represented by the number of underscores. If you guess a correct letter, the underscore will be 
replaced by the correct letter at the appropriate position. If your suggested letter is wrong and not 
present in the hidden word, this counts as a miss.

This game can be played both casually for a single round and competitively, where you have to win 3 rounds on the same 
level of difficulty to win a unique certificate. There are three different levels of difficulty, 
differing by the number of allowed misses. In the easy level you have a total of 8 misses, 
in the medium level 6 and in the difficult level 4. If you manage to correctly guess the word with fewer misses, 
you win. Otherwise you lose. Good luck!"""

# Casual, comp or tutorial (Do we need this?)
print("""This game can be played both casually for a single round and competitively, where you have to win 3 rounds 
on the same difficulty to win a unique certificate.\n\n\n""")


############ Defining functions for every part of the game ############

##### choosing the game mode #####
def mode_setter():

    # looping for tutorial and input validation purposes
    while True:

        game_mode = input("Choose a game mode: Single-round (S), Competition (C) or Tutorial (T)").upper()

        if game_mode == 'T':  # Shows the rules
            print(tutorial, "\n\n\n\n\n")

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

        # ask the player to choose the level of difficulty (easy, medium or difficult)
        difficulty = input('Please choose the level of difficulty: Easy (E), Medium (M) or Difficult (D) ')

        # if the input is correct continue with the game
        if difficulty.upper() in ('E', 'M', 'D'):
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

    # using conditionals, choose a random word from the corresponding list of words
    # depending on the difficulty level the player has a certain number of failed attempts at his/her disposal

    if difficulty.upper() == 'E':
        word = random.choice(words)
        max_number_of_misses = 8

    elif difficulty.upper() == 'M':
        word = random.choice(words)
        max_number_of_misses = 6

    elif difficulty.upper() == 'D':
        word = random.choice(words)
        max_number_of_misses = 4

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

        # checking for won round
        if "_" not in visible:
            won = 1
            break

        print("\n\n\n")
        print(*visible)
        print(f"\n\nWrong guesses: {*wrong_guesses,}   {max_number_of_misses - len(wrong_guesses)} remaining.\n\n")


        # checking if guess is valid
        guess = input("Please enter a letter to try: ").lower()

        if guess not in letters_possible:
            print("Please enter a valid letter.")

        elif guess not in letters:
            print("You have already guessed this letter.")

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
            print("You lost the game.")

        # print the correct word
        print("The correct word was:", word)


    else:  # competition mode

        if won == 1:

            # Print the correct word
            print("You won the round!\n\n")
            print("The correct word was:", word)

            # adjust number of rounds:
            num_games -= 1
            round_wins += 1

            if num_games > 0:
                print("\n\nNext round!\n\n")

        else:

            print("The correct word was:", word)
            print("You lost the game.")

            # adjust number of games:
            num_games = 0
            round_wins = 0


##### repeating the rounds for one total game #####
def game_flow():
    while num_games > 0:
        game_round()


############ starting the actual game ############

while repeat == 1:

    # comp or casual
    comp, num_games = mode_setter()

    # difficulty
    difficulty = choose_difficulty()

    # start the game
    game_flow()

    # certificate !!! Funktionen hinzufügen !!!
    if comp == 1 and round_wins == 3:
        print("CERTIFICATE")


    while True:

        # ask the player whether he/she wants to play again.
        # if YES, start the game again
        # if NO, end the game and thank the player for playing Hangman
        play_again = input('Do you want to play again? Input YES or NO: ').upper()
        if play_again == 'NO':
            repeat = 0
            break
        elif play_again == 'YES':
            break
        else:
            print("Please only input YES or NO.")




print("Thank you for playing Hangman!")
