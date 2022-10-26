import random
from wordlist import word
letter = ""
score = 6

print("Hi and welcome to the Hangman Game!\n")
name = input("What is your name: ").upper()
print("\nBest of Luck " + name)
print("\nThe Hangman Game is about to start.\n")

while score > 0:

    letter = input("Please guess a letter or a word: ")
    if letter in word:
        print(f"You have guessed correctly.{score} tries still left.")
    else:
        score = score - 1  # deducts a life if incorrect
        print(f"Your guess was incorrect. {score} tries left.")
        letter = letter + letter

    if letter in letter:
        print(f"you have already guessed this {letter}")
    elif letter not in word:
        print("letter is not in word.")
        letter.append(score)
