import random
import os
import subprocess

# Ask the player to enter his/her name and greet him/her
name = input('Please enter your name: ')
print('Hello' + ' ' + name + ',' + ' ' + "let's play Hangman!")


# Open the list with 999 common english words
with open('999 common english words.txt', 'r') as file:
    words = file.read().splitlines()

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

# to print a certificate if a certain condition is met we use an if statement

# certificate condition:
cert = 0
    
if cert == 0:

  # here we define the function for actually opening the certificate
  def open_certificate(certificate):
      # we need to differentiate the different commands for each operating system
      # to achieve this, we use if statements
      if os.name == 'nt':  # Windows
          with open('certificate.txt', 'w') as file:
              file.write(certificate)
          subprocess.run(['start', 'certificate.txt'], shell=True)
      elif os.name == 'posix':  # macOS or Linux
          with open('certificate.txt', 'w') as file:
              file.write(certificate)
          subprocess.run(['open', 'certificate.txt'])
      # if neither the Windows nor the macOS/Linux command is applicable we need to print an error message
      else:
          print("Unsupported operating system: cannot print the certificate.")

  # here we create the template for the certificate we want to generate
  # with curly brackets we can pass in variables which we want to to be included in the certificate
  certificate_template = """

  _____________________________________________________________________________________________________

  **************************************| Congratulations |********************************************

  _____________________________________________________________________________________________________


  You, {name}, have successfully completed our hangman game on difficulty {difficulty}!

  We hope you will play again soon!

  _____________________________________________________________________________________________________

  """

  # Generate the certificate by passing in the variables
  certificate = certificate_template.format(name=name, difficulty=difficulty)

  # Print the certificate by using the function defined earlier
  open_certificate(certificate)
  
else: print("To win a certificate, you need to win 3 games in a row. Better luck next time!")