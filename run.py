import random
import time
letter = ""
score = 6
play_game = "true"
play_game = "false"
true = ""
category = ""
x = "exit"
c = "colors"
cc = "characters"


print("Hi and welcome to the Hangman Game!\n")
time.sleep(1)
print("Object of the game is to guess the correct word chosen by the computer.")
print("The player can only guess one letter or word at a time.")
time.sleep(1)
name = input("\nWhat is your name: ").upper()
print("\nBest of Luck " + name)
time.sleep(1)
print("\nThe Hangman Game is about to start.\n")
time.sleep(1)

while score > 0:
    if category.upper() == "c":
        colors = random.choice("colors")
        break
    elif category.upper() == "cc":
        characters = random.choice("characters")
        break
    else:
        category = input("Please select a chosen category: c for colors / cc for characters; x for exit, _")
    if category == 'x':
        print("Goodbye, please visit again!")
        play_game = False
        break
    else:
        letter = input("Please guess a letter or a word: ")
    if letter in category:
        print(f"You have guessed correctly.{score} tries still left.")
    else:
        score = score - 1  # deducts a life if incorrect
        print(f"Your guess was incorrect. {score} tries left.")
        letter = letter + letter

    if letter in category:
        print(f"you have already guessed this {letter}")
    elif letter not in category:
        print("letter is not in word.")
      
