import random

word_list = ["python", "school", "science", "project", "hangman", "computer"]

secret_word = random.choice(word_list)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Guess the Word")

while wrong_guesses < max_wrong_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    if "_" not in display_word:
        print("You won! The word was:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if wrong_guesses == max_wrong_guesses:
    print("\nYou lost! The word was:", secret_word)