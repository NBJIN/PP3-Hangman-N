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
    Welcomes the player to hangman game and
    the player can choose wheather to play the game
    or choose a different level.
    """
    print(WELCOME)
    print("--------------------------------------------------")
    time.sleep(1)
    print("Instructions:")
    print("1. The object of the game is to guess the hidden word chosen by the Hangman program.")
    print("2. Each letter is represented by an underscore in the hidden word.")
    print("3. The player can only guess one letter or word at a time.")
    print("4. The program only accepts letter or words.  ")
    print("5. If the player chooses option 1 in the Menu section they are assigned 6 lives which is the default.")
    print("6. If the player chooses option 2 in the Menu section they can choose to play at the desired level.")
    print("7. If the player chooses A for level 1 - 4 lives is allocated to the player.")
    print("8. If the player chooses B for level 2 - 6 lives is allocated to the player.")
    print("9. Each player's successfull guess (letter or word) will reveal a underscore or the word")
    print("10. Should the player guess the word a message in ASCI text is displayed saying the player has won, congratulates the player and prints the correct guessed word")
    print("11. They player is then asked if they would like to play again")
    print("12. Choosing y will initiatite  a new game and choosing y will print game over in ASCII text to the terminal.")
    print("13. Confirmation of this success will be printed back to the player.")
    print("14. Each unsuccessfull guess the player looses a life, a message confirming same will be printed back to the user along with the number of lives and the next part of the hangman")
    print("15. Should the player run out of lives without guessing the word a message is printed back to the player advising them they have no more lives remaining ")
    print("16. A message is also displayed in ASCII text informing the player they have lost the game, the game has ended and prints the correct word.")
    print("17. It also asks the player wheather they would like to play again and if the player chooses y it starts the game all over again.")
    print("18. If the player chooses y a message in printed in ASCII Text to the terminal saying game over.")
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
            print(GAME_OVER)
            break

        elif setup == "2":
            print("Select Level\n")
            print("Choose A for level 1 which has 4 lives")
            print("Choose B for level 2 which has 6 lives")
            level = input("\n").upper()
            while level not in ["A", "B"]:
                print("Incorrect level selected. Please choose A or B.")
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
            else:
                lives = 6

                character = obtain_character()
                play_hangman(character, lives)
                while input("Would you like to play again? "
                            "(y/n) ").upper() in ["Y", "YES"]:
                    print("Start a new game")
                    character = obtain_character()
                    lives = 4
                    play_hangman(character, lives)
                print(GAME_OVER)

                break
        else:
            print("Error. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
