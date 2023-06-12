import random
import time
import score
from score import show_hangman
# from time import sleep
from wordlists import characters

# LETTER = ""
# SCORE = 6
# INCORRECT_SCORES = ""
# PLAY_GAME = "true"
# PLAY_GAME = "false"
# TRUE = ""
# CATEGORY = ""
# X = "exit"
# C = "colors"
# CC = "characters"
# HANGMAN = ""
# PRESENTLY = ""
# CHARACTERS = ""
# GAME_RUN = ""
# randomWord = ""
# COUNTER = ""
# wordlists = ""

# Welcome note to Hangman game
print("Welcome to the Hangman Game!\n")
print("--------------------------------------------------")
time.sleep(.05)
print("Instructions: guess the correct word chosen by the computer.")
print("The player can only guess one letter or word at a time.")
print("--------------------------------------------------")
time.sleep(.05)
name = input("\nWhat is your name: ").upper()
print("\nBest of Luck " + name)
print("--------------------------------------------------")
time.sleep(.05)
print("\nThe Hangman Game is about to start.\n")
print("--------------------------------------------------")
time.sleep(.05)

# Selecting a character


def obtain_character():
    """
    function to choose a character
    """
    character = random.choice(characters)
    return character.upper()

print(obtain_character())


def play(character):
    """
    function to play game
    """
    character_complete = "_" * len(character)
    guess = False
    guess_letters = []
    guess_characters = []
    lives = 6
    print(show_hangman(lives))
    print(character_complete)

    while not guess and lives > 0:
        guess = input("Please guess a letter or character: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guess_letters:
                print("This letter has been guessed already", guess)
            elif guess not in character:
                print(guess, "is not in the character.")
                lives -= 1
                guess_letters.append(guess)
            else:
                print("Congratulations,", guess, "is correct")
                guess_letters.append(guess)
                character_as_list = list(character_complete)
                indices = [i for i, letter in enumerate(characters) if letter == guess]
                for index in indices:
                    character_as_list[index] = guess
                character_complete = "".join(character_as_list)
                if "_" not in character_complete:
                    guess = True
                    break 

        elif len(guess) == len(character) and guess.isalpha():
            if guess in guess_characters:
                print("Character already guessed", guess)
            elif guess != character:
                print(guess, "is not the character.")
                lives -= 1
                guess_characters.append(guess)
            else:
                guess = True
                character_complete = character
                break

        else:
            print("Your guess is incorrect.")
        print(show_hangman(lives))
        print(character_complete)
        print("\n")

    if guess is True:
        print("Congratulations you guessed the character you have won this game")
    else:
        print("Im sorry you have ran out of lives.  The word was " + character + ". Please try again")

    return guess


def main():
    """
    function to play game again
    """
    character = obtain_character()
    play(character)
    while input("Would you like to play again? (Y/N) ").upper() in ["Y", "YES"]:
        character = obtain_character()
        play(character)


if __name__ == "__main__":
    main()

# """
# should be inside function under function name
# """

# while SCORE > 0:
#     if wordlists.upper() == "CC":
#         randomWord = random.choice("CATEGORY")
#         break
#     else:
#         wordlists = input("Select CATEGORY: CC for characters; X for exit, _")
#     if wordlists == 'X':
#         print("Goodbye, please visit again!")
#         PLAY_GAME = False
#         break
#         print("----------")
#     for LETTER in wordlists:
#         LETTER = input("Please guess a letter in characters: \n")
#         print(f"\nGuess is correct, there is a {LETTER} in the word.")
#         print("----------")

#     def printWord(letter):
#             COUNTER = 0
#             SCORE = 0
#         for LETTER in randomWord:
#             if (LETTER in LETTER):
#                     print(randomWord[COUNTER], end="")
#                 SCORE += 1
#             else:
#                 print(" ", end=" ")
#                 COUNTER += 1
#                 return SCORE
#     for LETTER in CHARACTERS:
#         print(f"Your guess was incorrect. {SCORE} tries left.")
#         SCORE = SCORE - 1  # deducts a life if incorrect
#         LETTER = LETTER + LETTER
#     while LETTER in CHARACTERS:
#         print("Sorry you have already guessed this {letter}")
# else:
#     LETTER not in CHARACTER
#     print("letter is not in word.")
#     if SCORE == SCORE:
#         print(HANGMAN, [SCORE])
#         print("\nYou've been hanged!")
#     else:
#         print("\nYou guessed it!")
#         print("\nThe word was, {characters}")
#         input("n\nPress the enter key to exit")

#     def play_again():
#         response = input("Play again? Enter y = yes or n = no")

#         if response == 'y':
#             GAME_RUN()

#     """.git/else:
#         for x in randomWord:
#             print("_", end="")
    # def print_hangman(wrong):
    #     if (wrong == 0):
    #         print("\n ---------")
    #         print("   | /  |")
    #     elif (wrong == 1):
    #         print("\n ---------")
    #         print("   | /  |")
    #         print("   |/   O")
    #     elif (wrong == 2):
    #         print("\n+++---------+++")
    #         print("   | /  |")
    #         print("   |/   O")
    #         print("   |  \\ ")
    #     elif (wrong == 3):
    #         print("\n ---------")
    #         print("   | /  |")
    #         print("   |/   O")
    #         print("   |  \\ //")
    #     elif (wrong == 4):
    #         print("\n ---------")
    #         print("   | /  |")
    #         print("   |/   O")
    #         print("   |  \\ //")
    #         print("   |    |")
    #     elif (wrong == 5):
    #         print("\n ---------")
    #         print("   | /  |")
    #         print("   |/   O")
    #         print("   |  \\ //")
    #         print("   |    |")
    #         print("   |  //")
    #         print("   |")
    #     elif (wrong == 6):
    #         print("\n ---------")
    #         print("   |  / |")
    #         print("   | /  O")
    #         print("   |  \\ //")
    #         print("   |    |")
    #         print("   |  // \\")
    #         print("   | ")
