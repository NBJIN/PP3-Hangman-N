import random
import time
# import score
from score import show_hangman
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


# def obtain_letter():
    """
    function to choose a character
    """
    # letter = random.choice(characters)
    # return letter.upper()
    # return letter


print(obtain_character())
# print(obtain_letter())


def play_hangman(character):
    """
    function to play game
    """
    character = obtain_character()
    character_complete = "_" * len(character)
    # character = character.upper()
    success = False
    player_guess = []
    guess_letters = []
    guess_characters = []
    lives = 6

    print(show_hangman(lives))
    print(character_complete)

    while not success and lives > 0:
        player_guess = input("Please guess a letter or character: ").upper()
        # player_guess = input("Please guess a letter or character: ")

        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guess_letters or player_guess in guess_characters:
                print("This letter has been guessed already", player_guess)
            elif player_guess not in character_complete:
                print(player_guess, "is not in the character.")
                lives -= 1
                guess_letters.append(player_guess)
            else:
                print("Congratulations,", player_guess, "is correct")
                guess_letters.append(player_guess)
                character_as_list = list(character_complete)
                indices = [i for i, letter in enumerate(character.upper()) if letter == player_guess]
                for index in indices:
                    character_as_list[index] = player_guess
                character_complete = "".join(character_as_list)
                if "_" not in character_complete:
                    success = True
                    break

        elif len(player_guess) == len(character) and player_guess.isalpha():
            if player_guess in guess_characters:
                print("Character already guessed", player_guess)
            elif player_guess.upper() != character:
                print(player_guess, "is not the character.")
                lives -= 1
                guess_characters.append(player_guess)
            else:
                success = True
                character_complete = character
                break

        else:
            print("Your guess is incorrect.")
            lives -= 1
        print(show_hangman(lives))
        print(character_complete)
        print("\n")

    if success:
        print("Congratulations you guessed the character you have won this game")
    else:
        print("Im sorry you have ran out of lives.  The word was " + character + ". Please try again")

    return success


def main():
    """
    function to play game again
    """
    character = obtain_character()
    play_hangman(character)
    while input("Would you like to play again? (y/n) ").upper() in ["y", "yes"]:
        character = obtain_character()
        play_hangman(character)


if __name__ == "__main__":
    main()
