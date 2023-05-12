import random

# Ask the player to enter his/her name and greet him/her
name = input('Please enter your name: ')
print('Hello' + ' ' + name + ',' + ' ' + "let's play Hangman!")


# Open the list with 999 common english words
with open('999 common english words.txt', 'r') as file:
    words = file.read().splitlines()
    
# Create three empty lists for the three different levels of difficulty
easy_words = []
medium_words = []
difficult_words = []

# Filter the words list '999 common english words' using a loop
# Add all words to the corresponding list
# Hier noch anzupassen, wieviele Buchstaben für welchen Schwierigkeitsgrad
for word in words:
    if len(word) == 4:
        easy_words.append(word)
    elif len(word) == 6:
        medium_words.append(word)
    elif len(word) == 8:
        difficult_words.append(word)


# Ask the player to choose the level of difficulty (easy, medium or difficult)
difficulty = input('Please choose the level of difficulty: Easy (E), Medium (M) or Difficult (D) ')

# Using conditionals, choose a random word from the corresponding list of words               
if difficulty.upper() == 'E':
    word = random.choice(easy_words)
elif difficulty.upper() == 'M':
    word = random.choice(medium_words)
elif difficulty.upper() == 'D':
    word = random.choice(difficult_words)
else:
    print('Error - Wrong input')
