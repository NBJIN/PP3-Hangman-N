import random
import time
LETTER = ""
SCORE = 6
INCORRECT_SCORES = ""
PLAY_GAME = "true"
PLAY_GAME = "false"
TRUE = ""
CATEGORY = ""
X = "exit"
C = "colors"
CC = "characters"
HANGMAN = ""
PRESENTLY = ""
CHARACTERS = ""
GAME_RUN = ""
randomWord = ""
COUNTER = ""

# welcome / greeting
print("Welcome to the Hangman Game!\n")
time.sleep(1)
print("Instructions: guess the correct word chosen by the computer.")
print("The player can only guess one letter or word at a time.")
time.sleep(1)
name = input("\nWhat is your name: ").upper()
print("\nBest of Luck " + name)
time.sleep(1)
print("\nThe Hangman Game is about to start.\n")
time.sleep(1)

# choose a random word
while SCORE > 0:
    if CATEGORY.upper() == "cc":
        randomWord = random.choice("characters")
        break
    else:
        characters = input("Select category: cc for characters; x for exit, _")
    if characters == 'x':
        print("Goodbye, please visit again!")
        PLAY_GAME = False
        break
        print("----------")
    for letter in characters:
        letter = input("Please guess a letter in characters: \n")
        print(f"\nGuess is correct, there is a {letter} in the word.")
        print("----------")
    else:
        for x in randomWord:
            print("_", end="")
    def print_hangman(wrong):
        if (wrong == 0):
            print("\n ---------")
            print("   | /  |")
        elif (wrong == 1):
            print("\n ---------")
            print("   | /  |")
            print("   |/   O")
        elif (wrong == 2):
            print("\n +++---------+++) 
            print("   | /  |")
            print("   |/   O")
            print("   |  \\ ")
        elif (wrong == 3):
            print("\n ---------")
            print("   | /  |")
            print("   |/   O")
            print("   |  \\ //")
        elif (wrong == 4):
            print("\n ---------")
            print("   | /  |")
            print("   |/   O")
            print("   |  \\ //")
            print("   |    |")       
        elif (wrong == 5):
            print("\n ---------")
            print("   | /  |")
            print("   |/   O")
            print("   |  \\ //")
            print("   |    |")
            print("   |  //")
            print("   |")
        elif (wrong == 6):
            print("\n ---------")
            print("   |  / |")
            print("   | /  O")
            print("   |  \\ //")
            print("   |    |")
            print("   |  // \\")
            print("   | ")
      
    def printWord(letter):
            COUNTER = 0
            SCORE = 0
            for letter in randomWord:
                if (letter in letter):
                    print(randomWord[COUNTER], end="")
                SCORE += 1
            else:   
                print(" ", end=" ")
                COUNTER += 1
                return SCORE
                break

    for letter in characters:
        print(f"Your guess was incorrect. {SCORE} tries left.")
        SCORE = SCORE - 1  # deducts a life if incorrect
        letter = letter + letter
    while letter in characters:
        print("Sorry you have already guessed this {letter}")

else:
    letter not in characters
    print("letter is not in word.")
    if SCORE == SCORE:
        print(HANGMAN, [SCORE])
        print("\nYou've been hanged!")
    else:
        print("\nYou guessed it!")
        print("\nThe word was, {characters}")
        input("n\nPress the enter key to exit")

    def play_again():
        response = input("Play again? Enter y = yes or n = no")

        if response == 'y':
            GAME_RUN()
