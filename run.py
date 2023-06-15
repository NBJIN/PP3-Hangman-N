
"""
Libraries and imports
"""
import random
import time
# import score
from score import show_hangman
from score import win
# from time import sleep
from wordlists import characters


# Welcome note to Hangman game
print("Welcome to the Hangman Game!\n")
print("--------------------------------------------------")
time.sleep(1)
print("Instructions: guess the correct word chosen by the computer.")
print("The player can only guess one letter or word at a time.")
print("All enteries to be made in uppercase")
print("--------------------------------------------------")
time.sleep(1)
name = input("\nWhat is your name: ").upper()
print("\nBest of Luck " + name)
print("--------------------------------------------------")
time.sleep(1)
print("\nThe Hangman Game is about to start.\n")
print("--------------------------------------------------")
time.sleep(1)

# Selecting a character


def obtain_character():
    """
    function to choose a character
    """
    character = random.choice(characters)
    return character.upper()
    # return character


# print(obtain_character())


def play_hangman(character, lives):
    """
    function to play game
    """
    # # character = obtain_character()
    # character = character_complete.upper()
    character_complete = "_" * len(character)
    # character = character.upper()
    success = False
    player_guess = []
    # guess_letters = []
    guess_characters = []
    # tries = []
    lives = 6

    print(show_hangman(lives))
    print(character_complete)
    print(character)

    while not success and lives > 0:
        player_guess = input("Please guess a letter or character: ").upper()
        # player_guess = input("Please guess a letter or character: ")
        try:
            if len(player_guess) == 1 and player_guess.isalpha():
                if player_guess in guess_characters:
                    print("This letter has been guessed already", player_guess)
                elif player_guess not in character:
                    print(player_guess, "is not in the character.")
                    print("You loose a life")
                    lives -= 1
                    print(f"You have {lives} lives remaining")
                    guess_characters.append(player_guess)
                else:
                    print("Congratulations,", player_guess, "is correct")
                    guess_characters.append(player_guess)
                    character_as_list = list(character_complete)
                    indices = [
                        i for i, letter in enumerate(character)
                        if letter == player_guess and
                        character_complete[i] == "_"
                    ]
                    for index in indices:
                        character_as_list[index] = player_guess
                    character_complete = "".join(character_as_list)
                    # if "_" not in character_complete.replace(player_guess, '') and all(letter != "_" for letter in character_complete):
                    if "_" not in character_complete:
                        success = True
                        break

            elif len(player_guess) == len(character) and \
                    player_guess.isalpha():
                if player_guess in guess_characters:
                    print("Character already guessed", player_guess)
                elif player_guess.upper() != character:
                    print(player_guess, "is not the character.")
                    lives -= 1
                    print(f"You have {lives} lives remaining")
                    guess_characters.append(player_guess)
                else:
                    success = True
                    character_complete = character
                    break

            else:
                print("Your guess is incorrect.")
                lives -= 1
                print(f"You have {lives} lives remaining")
            print(show_hangman(lives))
            print(character_complete)
            print("\n")

        except ValueError:
            print("Invalid input. Please try again.")

    if success:
        print("Congratulations you guessed the character "
              + character_complete + " you have won this game")
    else:
        print("The game has now ended. "
              "The word was ", character)
        print("Please try again")

    # print(character_complete)

    return success


def main():
    """
    function to play game again
    """
    character = obtain_character()
    lives = 6
    play_hangman(character, lives)
    while input("Would you like to play again? "
                "(y/n) ").upper() in ["Y", "YES"]:
        print("Start a new game")
        character = obtain_character()
        lives = 6
        play_hangman(character, lives)


if __name__ == "__main__":
    main()
