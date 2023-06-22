"""
pp3
libraries and imports
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
    clear terminal
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

    while not success and lives > 0:
        player_guess = input("Please guess a letter or word: ").upper()
        if not player_guess.isalpha():
            print("Error: The Hangman game only accepts letters or words.")
        try:
            if len(player_guess) == 1 and player_guess.isalpha():
                if player_guess in guess_characters:
                    print("This letter has been guessed already", player_guess)
                elif player_guess not in character:
                    print(player_guess, "is not in the word.")
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
                    print("This guess has  already been guessed", player_guess)
                elif player_guess.upper() != character:
                    print(player_guess, "is not the word.")
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
        print("Congratulations you guessed the word "
              + character_complete + " you have won this game")
    else:
        print(LOOSE)
        print("The game has now ended. "
              "The word was ", character)
        print("Please try again")
    return success


def main():
    """
    welcomes the player to hangman game and
    the player can choose wheather to play the game
    or choose a different level.
    """
    print(WELCOME)
    print("--------------------------------------------------")
    time.sleep(1)
    print("Instructions:")
    print("1. The object of the game is to guess the hidden word.")
    print("2. Each letter is represented by an underscore in the hidden word.")
    print("3. The player can only guess one letter or word at a time.")
    print("4. The program only accepts letters or words.  ")
    print("5. The player can choose option 1 or 2 in the Menu section")
    print("6. Option 1 is assigned 6 lives which is the default.")
    print("7. Option 2 in the Menu section offers a desired level.")
    print("8. A is assigned 4 lives.")
    print("9. B is assigned 6 lives.")
    print("10. Each successful guess will reveal an underscore or the word.")
    print("11. Message saying you won is displayed if word is guessed.")
    print("11. The player is then asked if they would like to play again")
    print("12. Choosing y starts a new game.")
    print("13. choosing n will print game over.")
    print("14. Each unsuccessfull guess the player looses a life.")
    print("15. A message confirming same will be printed back to the user.")
    print("16. The no. of lives and the hangman stage is also printed.")
    print("17. If the player run out of lives without guessing the word")
    print("    a message is printed back to the player advising them they")
    print("     have no more lives left.")
    print("18. A message is also displayed saying You Loose.")
    print("19. It also advises the game has ended.")
    print("20. The player is asked if they would like to play again.")
    print("21. If n is chosen a message prints game over.")
    print("22. If player chooses y game starts all over again.")
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
            while True:
                play_again = input("Would you like to play again? "
                                   "(y/n) ").upper()
                if play_again == "Y":
                    print("Start a new game")
                    character = obtain_character()
                    lives = 6
                    play_hangman(character, lives)
                elif play_again == "N":
                    print(GAME_OVER)
                    break
                else:
                    print("Error please enter y or n")

        elif setup == "2":
            print("Select Level\n")
            print("Choose A if you wish to play with 4 lives")
            print("Choose B if you wish to play with 6 lives")
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

            while True:
                play_again = input("Would you like to play "
                                   "again? (y/n) ").upper()
                if play_again == "Y":
                    print("Start a new game")
                    character = obtain_character()
                    lives = 4
                    play_hangman(character, lives)
                elif play_again == "N":
                    print(GAME_OVER)
                    break
                else:
                    print("Invalid input. Please enter y or n.")
        else:
            print("Error. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
