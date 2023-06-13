import random


# List of ASCII art for the hangman game
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Grab word from wordbank.txt and uppercase
def wordlist():
    with open("wordbank.txt", "r") as f:
        wordbank = f.read().split(",")
    global word
    word = random.choice(wordbank).upper()

# Let user enter name as username
def username():
    name = input("What is your name?: ")
    print("Hello " + name + ",", "are you able to guess the word?")


def guesswords():
    # Initialize variables
    guesses = ''
    attempts = 7
    hang = -1

    # Loop until attempts run out
    while attempts > 0:
        failed = 0

        # Check if each letter in word has been guessed
        for letter in word:
            if letter in guesses:
                print(letter, end="")
            else:
                print("_", end="")
                failed += 1

        # If no letters are left to guess, player wins
        if failed == 0:
            print("\nYou won!")
            break

        # Get player's guess
        guess = input(" Guess a letter or the whole word: ").upper()

        # If player guesses a single letter
        if len(guess) == 1:
            # Check if letter has already been guessed
            if guess in guesses:
                print("You already guessed that letter!")
            else:
                # Add guess to list of guesses
                guesses += guess

                # Check if guess is correct
                if guess in word:
                    print("Correct!")
                else:
                    print("Wrong!")
                    attempts -= 1
                    hang += 1
                    print(HANGMANPICS[hang])

        # If player guesses the whole word
        elif len(guess) == len(word):
            if guess == word:
                print("You guessed the word!")
                print("You won! ")
                break
            else:
                print("That's not the word!")
                attempts -= 1
                hang += 1
                print(HANGMANPICS[hang])
        else:
            print("Please enter a single letter or the whole word!")

        # If attempts run out, player loses
        if attempts == 0:
            print("You lose!")
            print("The word was:", word)

# call functions
def functions():
    username()
    wordlist()
    guesswords()


functions()
