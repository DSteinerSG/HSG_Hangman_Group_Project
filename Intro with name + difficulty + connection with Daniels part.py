import random

# Ask the player to enter his/her name and greet him/her
name = input('Please enter your name: ')
print('Hello' + ' ' + name + ',' + ' ' + "let's play Hangman!")


# Open the list with 999 common english words
with open('999 common english words.txt', 'r') as file:
    words = file.read().splitlines()


# Ask the player to choose the level of difficulty (easy, medium or difficult)
while True:
    difficulty = input('Please choose the level of difficulty: Easy (E), Medium (M) or Difficult (D) ')
    
    if difficulty.upper() in ('E', 'M', 'D'):
        break
    else:
        print('Wrong input. Please enter a valid level of difficulty.')

# Using conditionals, choose a random word from the corresponding list of words
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

else:
    print('Error - Wrong input')



# visible word:
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
    print("The correct word was:", word)

else:
    print("You lost the game.")
    print("The correct word was:", word)


# prevents console closing:
con = input("Thank you for playing Hangman!")
