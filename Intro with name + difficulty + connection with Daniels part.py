import random

# Ask the player to enter his/her name and greet him/her
name = input('Please enter your name: ')
print('Hello' + ' ' + name + ',' + ' ' + "let's play Hangman!")


# Open the list with 999 common english words
with open('999 common english words.txt', 'r') as file:
    words = file.read().splitlines()

# tutorial file
tutorial = "empty"
    
    
# Casual, comp or tutorial
print("""This game can be played both casually for a single round and competitively, where you have to win 3 rounds 
on the same difficulty to win a unique certificate.\n\n\n""")


while True:

    game_mode = input("Choose a game mode: Single-round (S), Competition (C) or Tutorial (T)").upper()
    if game_mode == 'T':
            print(tutorial, "\n\n\n\n\n")

    elif game_mode == 'S':
        comp = 0
        break

    elif game_mode == 'C':
        comp = 1
        break

    else:
        print("\n\n\nPlease enter a valid input.\n\n\n")


# Start a loop for the game
while True:
    
    
    while True:
        # Ask the player to choose the level of difficulty (easy, medium or difficult)
        difficulty = input('Please choose the level of difficulty: Easy (E), Medium (M) or Difficult (D) ')
    
        # If the input is correct continue with the game
        if difficulty.upper() in ('E', 'M', 'D'):
            break
        
        # If the input is wrong, ask the player to enter a valid level of difficulty
        else:
            print('Wrong input. Please enter a valid level of difficulty.')

    # Using conditionals, choose a random word from the corresponding list of words
    # Depending on the difficulty level the player has a certain number of failed attempts at his/her disposal
    # Anzahl von Fehlversuchen je Schwierigkeitsgrad noch festzulegen
    if difficulty.upper() == 'E':
        word = random.choice(words)
        max_number_of_misses = 8

    elif difficulty.upper() == 'M':
        word = random.choice(words)
        max_number_of_misses = 6

    elif difficulty.upper() == 'D':
        word = random.choice(words)
        max_number_of_misses = 4

   
    # visible wordD:
    visible = ["_" for n in range(len(word))]

    # Turn-timer (difficulty-dependent):


    # win condition:
    won = 0

    # count wrong_guesses:
    wrong_guesses = []

    # letter-list:
    letters_possible = list("abcdefghijklmnopqrstuvwxyz")
    letters = list("abcdefghijklmnopqrstuvwxyz")

    while len(wrong_guesses) < max_number_of_misses:

        print("\n\n\n")
        print(*visible)
        print(f"\n\nWrong guesses: {*wrong_guesses,}\n\n")

        if "_" not in visible:
            won = 1
            break

        guess = input("Please enter a letter to try: ").lower()

        if guess not in letters_possible:
            print("Please enter a valid letter.")

        elif guess not in letters:
            print("You have already guessed this letter.")

        else:
            letters.remove(guess)

            for char in range(len(word)):

                if guess == word[char]:
                    visible[char] = guess

            if guess not in word:
                wrong_guesses.append(guess)


    if won == 1:
        print("You won the game!")

    else:
        print("You lost the game.")

    # Print the correct word
    print("The correct word was:", word)

    # Ask the player whether he/she wants to play again.
    # If YES, start the game where the player can choose the level of difficulty
    # If NO, end the game and thank the player for playing Hangman
    play_again = input('Do you want to play again? Input YES or NO: ').upper()
    if play_again != 'YES':
        break

print("Thank you for playing Hangman!")
