# word_choice (example):
word = "again"
word = list(word)

# visible word:
visible = ["_" for n in range(len(word))]

# Turn-timer (difficulty-dependent):
turns = 10

# win condition:
won = 0

# count wrong_guesses:
wrong_guesses = []

# letter-list:
letters_possible = list("abcdefghijklmnopqrstuvwxyz")
letters = list("abcdefghijklmnopqrstuvwxyz")

while len(wrong_guesses) < turns:

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


if won = 1:
    print("You won the game!")
else:
    print("You lost the game.")

