
word = "giraffe"
guesses = 6



while guesses > 0:
    guesses = input("Enter a letter or a word: ")

    if guesses in word:
        print("Well done you have guessed correctly.")
    else:
        guesses -= 1
        print(f"Your guess was incorrect. {noofplays} left.")

        guesses = guesses + 1

    for letter in word:
        if letter in word:
            print(f"{word}")
    else:
        print("_", end = " ")
        guesses += 1

    if guesses == 0:
        print(f"Well Done the word was {word}. You won!")
        break

    else:
        print("Sorry You Lost, Please try again.")

