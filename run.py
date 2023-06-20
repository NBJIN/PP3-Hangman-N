"""
Portfolio Project 3

Libraries and imports
"""
import random
import time
import os
from score import (
    show_hangman,
    WIN,
    LOOSE,
    WELCOME,
    GAME_OVER,
    )
# from time import sleep
from wordlists import characters


def clear_terminal():
    """
    Clear terminal
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear_terminal()


def obtain_character():
    """
    function to choose a character
    """
    character = random.choice(characters)
    return character.upper()


def play_hangman(character, lives):
    """
    function to play game
    """
    character_complete = "_" * len(character)
    success = False
    player_guess = []
    guess_characters = []

    print(show_hangman(lives))
    print(character_complete)
    print(character)

    while not success and lives > 0:
        player_guess = input("Please guess a letter or character: ").upper()
        if not player_guess.isalpha():
            print("Error: The Hangman game only accepts letters or words.")
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
        print(WIN)
        print("Congratulations you guessed the character "
              + character_complete + " you have won this game")
    else:
        print(LOOSE)
        print("The game has now ended. "
              "The word was ", character)
        print("Please try again")
    return success


def main():
    """
    Welcome player to hangman and
    they can choose wheater to play the game
    or choose a different level.
    """
    print(WELCOME)
    print("--------------------------------------------------")
    time.sleep(1)
    print("Instructions:")
    print("Guess the correct word chosen by the Hangman program.")
    print("The player can only guess one letter or word at a time.")
    print("All enteries to be made in uppercase")
    print("The program only accepts letters or words.  ")
    print("--------------------------------------------------")
    time.sleep(1)
    print("MENU")
    time.sleep(1)
    print("Choose " + "1" + " To Start Playing The Hangman Game")
    print("Choose " + "2" + " To Choose The Desired Level")
    print("--------------------------------------------------")

    while True:
        setup = input("\n")
        if setup == "1":
            time.sleep(1)
            name = input("\nWhat is your name: ").upper()
            print("\nBest of Luck " + name)
            print("--------------------------------------------------")
            time.sleep(1)
            print("\nThe Hangman Game is about to start.\n")
            print("--------------------------------------------------")
            time.sleep(1)

            character = obtain_character()
            lives = 6
            play_hangman(character, lives)
            while input("Would you like to play again? "
                        "(y/n) ").upper() in ["Y", "YES"]:
                print("Start a new game")
                character = obtain_character()
                lives = 6
                play_hangman(character, lives)
            # if input("Would you like to play again? "
            #          "(y/n) ").upper() in ["N", "NO"]:


            # play_game = ""
            # while play_game not in ["Y", "YES", "N", "NO"]:
            #     play_game = input("Would you like to play again? (y/n): ").upper()

            # if play_hangman in ["N", "NO"]:
            # while input("Would you like to play again? "
            #             "(y/n) ").upper() in ["N", "NO"]:
            print(GAME_OVER)
            break

        elif setup == "2":
            print("Select Level\n")
            print("Choose A for level 1 which has 4 lives")
            print("Choose B for level 2 which has 6 lives")
            level = input("\n").upper()
            while level not in ["A", "B"]:
                print("Incorrect level selected. Please try again.")
                level = input().upper()
            time.sleep(1)
            name = input("\nWhat is your name: ").upper()
            print("\nBest of Luck " + name)
            print("--------------------------------------------------")
            time.sleep(1)
            print("\nThe Hangman Game is about to start.\n")
            print("--------------------------------------------------")
            time.sleep(1)

            if level == "A":
                lives = 4
                character = obtain_character()
                play_hangman(character, lives)
                while input("Would you like to play again? "
                            "(y/n) ").upper() in ["Y", "YES"]:
                    print("Start a new game")
                    character = obtain_character()
                    lives = 4
                    play_hangman(character, lives)
                print(GAME_OVER)
            elif level == "B":
                lives = 6
                character = obtain_character()
                play_hangman(character, lives)
                while input("Would you like to pay again? "
                            "(y/n) ").upper() in ["Y", "YES"]:
                    print("Start a new game")
                    character = obtain_character()
                    lives = 6
                    play_hangman(character, lives)
                print(GAME_OVER)
            # else:
            #     print("Incorrect level selected. Please try again.")

            #     print("\nPlease Choose A or B")


if __name__ == "__main__":
    main()
