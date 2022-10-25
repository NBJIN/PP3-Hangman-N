import random
from word import word

# Variables 
Guesses_Guessed = ""
Guesses_Not_Guessed = ""
No_of_Plays = 6


# Introduction To Game
print("Hi and welcome to the Hangman Game!")
name = input("What is your name: ").upper()
print("Best of Luck " + name)
print("The Hangman Game is about to start.")


# Function Get Random Word


def getRandomWord(word):
    word = random.choice(word)
    while '_' in word or ' ' in word:
        No_of_Plays = 6
        return word.upper
        print("word")


# Function play game


def playGame(word):
    while No_of_Plays and Guesses > 0:
        guesses = input("Please guess a letter or word: ").upper()
        if guesses in word:
            print(f"well done you have guessed correctly.")
        else:
            No_of_Plays -= 1 # Deducts a life if incorrect.
            # let user know no of lives left if inocrrect
            print(f"Your guess was incorrect. You have {No_of_Plays} left.") 

        Guesses_Guessed = Guesses_Guessed + Guesses_Guessed
        incorrrect_Guesses = 0

        for letter in word:
            if letter or word in word:
                print(f"{letter}", end="")
            else:
                print("_", end = "")
                incorrrect_Guesses += 1

        if incorrrect_Guesses == 0:
            print(f"The correct word was: (word). You beat the hangman!")
            break

    else:
        if incorrrect_Guesses == 0:
            print(f"You did not win this game.")
            playGame = input("Would you like to play again? y = yes, n = no")