import random


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def wordlist():
    with open("wordbank.txt", "r") as f:
        wordbank = f.read().split(",")
    global word
    word = random.choice(wordbank).upper()

def username():
    name = input("What is your name?: ")
    print("Hello " + name + ",", "are you able to guess the word?")


def guesswords():
    guesses = ''
    attempts = 7
    hang = -1
    while attempts > 0:
        failed = 0
        for letter in word:
            if letter in guesses:
                print(letter, end="")
            else:
                print("_", end="")
                failed += 1
        if failed == 0:
            print("\nYou won!")
            break
        guess = input(" Guess a letter or the whole word: ").upper()
        if len(guess) == 1:
            if guess in guesses:
                print("You already guessed that letter!")
            else:
                guesses += guess
                if guess in word:
                    print("Correct!")
                else:
                    print("Wrong!")
                    attempts -= 1
                    hang += 1
                    print(HANGMANPICS[hang])
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
        if attempts == 0:
            print("You lose!")
            print("The word was:", word)


def functions():
    username()
    wordlist()
    guesswords()


functions()
