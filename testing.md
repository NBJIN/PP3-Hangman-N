[Link Back To Main Readme Document](README.md)

## 5 Testing 
<br>

### Testing of Developer / Owner Goals and Player / User Goals - Manual Testing
<br>

| Goals | Acceptance | Pass | Fail |
|:--------|:-------|:-------|:------|
| Developer / Owner Goals   |  |  |  |
| 1.  Offer entertainment to the player who wants to play the game   | The hangman game has a very user friendly interface which makes the game enjoyable and fun to play. | Pass |  |
| 2.  It should have clear instructions displayed to player    | When the Hangman game commences it displays a full list of instructions to the player which are very clear and detailed. | Pass |  |
| 3.  To allow the user interact with the game by adding inputs to questions and guesses for words.    | The hangman game allows the player to start the game or choose a level at the start.  It also allows the player to enter a guess in letter or word format  | Pass |  |
| Player / User Goals    |  |  |  |
| 1.  The game should be easy to play    | The interface of the hangman game is very easy to use and engage with as a player.  | Pass |  |
| 2.  It should have clear instructions displayed to the player  | When the game commences it displays a full set of instructions to the player so that they know exactly how to play the game.   | Pass |  |
| 3.  The game should be fun and engaging   | The game allows the player to choose a level, allows the player to guess either by letter or word and also allows the user to test their guessing ability with different levels which makes it fun and engaging.  | Pass  |  |
| 4.  Easy navigation throughout the game  | The hangman game is very easy to navigate. It prompts the user for their input at every step making it very easy to naviage for the user.  | Pass |  |
| 5.  Be challenging by providing different player levels   | In the menu section of the game when the player chooses 2 it splits into A and B where if the player chooses A they play with 4 lives and B plays with 6 lives | Pass |  |

### Testing of Features and Validation - Manual Testing
- Start Game

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/abdd8f4a-021c-4468-b328-d92ed81cf362)

When the player clicks on Run Program on Heroku it runs the game and the player can see the Welcome banner "Welcome To Hangman".  It then displays a list of instructions which explains exactly how to play the game.  In the Menu section the player can choose 1 to start playing the hangman game or 2 to choose a desired level. 

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/a8212703-c927-4940-af6f-cc79d0931c5b)
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/f8a82527-4800-47fd-95ea-55cc0df97d67)
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/8e4ce074-520c-4ede-ac68-83946cf18af7)

<br>
- In Gitpod the player will type "python3 run.py" in the terminal and this will run the program and displays the exact details like when the program in run in Heroku (see above). 
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/729ca7a7-9a5d-4324-a719-a5f7dd387011)
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/0783391a-0df1-4d9b-95a2-b4c5e4f03de8)
<br>

- The information displayed and steps are the same in Heroku and Gitpod from this point onwards. 

- Validation - If the player inputs a different no, letter  or special character the Hangman Program will print an error. 

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/2eb1ed35-3b12-4398-b460-82a6243768a6)

- When the player chooses the number 1 in the Menu Section the game will begin where it asks the player for their name and wishes them the best of luck.  (For the purposes of testing i have the random word printed to the terminal just for validation purposes this will not be printed in the actual game.) The start of the hangman displays and underscores are printed to represent the hidden word.  The player is then asked to enter a letter or word.

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/addfeca7-2af9-4e2d-a269-1438bb551142) 

 - If the player does not enter a letter or word a message will print back to the player that the Hangman game only accepts letters or words, guess is incorrect and it deducts a life.

 <br> 
 Tested with numbers

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/4bdc2311-4574-49c8-aa58-d3b6545e0f6a)

 <br>
 Tested with special characters

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/a62d9df0-d046-4d6e-b556-4ead043e440b)

 - When the player enters a correct guess a message of congratulations is displayed back to the player and asks the player to guess another word.  

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/0a626e1a-a184-4526-ade3-eb8b7d0c4ba0)

 - If the player guesses all letters/word correctly ASCII text of "You Win" is displayed back to the user along with a message that congratulates the user and displays the correct word again.  The player is also asked wheather they would like to play the game again.  

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/dc4af21e-1500-4744-a10b-96bd676bee3e)

 - Should the player enter a differnt character besides y or n to play the game again it will print an error.

 <br>

 Error which appears when different letters, numbers and special characters are entered.

 <br>

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/7d04db2b-15ef-4758-a5cf-3737ac18e954)

 - When the player enters y it will start the new game. 

 <br>

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/52733a79-2dde-4bd6-a270-1e039f904078)

 <br>

 - When the player enters n it will print game over.

 <br>

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/a8b0239d-255e-4d75-bc80-2fdb090e922f)

 <br>

 - When the player enters 2 to choose the desired level on the menu section two options will be presented to them.  The player can choose A if they wish to play with 4 lives or B if they wish to play with 6 lives.

 <br>

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/adee0a9a-82be-4ced-b856-c17ea0eae755)

 - If the player does not make the correct input of A or B the game will print an error.

 <br>

 Error response when incorrect letter, number and special character is entered. 

 <br>

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/cbf7b2e2-6b73-4e03-ac03-835e3e871bf4)  

 <br>

 - When the player enters A it will start the game with 4 lives where it asks the player  for their name, wishes the player best of luck and informs the player the game is about to start. It also prints the hangman with a head and one arm as A plays with four lives which leaves the second arm, body and both legs to be filled in and this makes up the four lives.  It also prints the underescores for the word and asks the player to guess a letter or word .
 <br>

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/9476919f-1588-4aa6-a17d-6c1d173ac254)

 <br>

 - If the player enters anything other than a letter or word it will print an error back to the user and they loose a life.

 <br>

 Error that shows that numbers or special characters are not accepted.

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/c61a6763-3406-4f59-8d28-87d8befad9be)

 <br>

 - When the player guesses the correct word you win is printed with a message congratulating the player and prints the correct word and advises the player they have won the game.  Here it also asks the player wheather they would like to play the game again. 

 <br>

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/ec04ba13-1915-4781-8dc9-9b7c5bb189c9)

 <br>

 - When the game asks the player if they would like to play again it expects the user to enter either y or n.  If the user prints somthing different it will print and error back to the playeer.  

 <br>

 Error which displays when an incorrect letter, number or special character is entered. 

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/0ee948a4-2099-4e95-ad7e-62a4f717dbe8)

 <br>

 - When the user chooses y the game will start all over again.

 <br>

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/5c152691-dd82-4ec6-953b-74df5385d320)

 <br>

 - When the user chooses n the game will end.

 <br>

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/859b6a54-0b9e-4406-a65b-3665ecde3bda)

 <br>

 - When the user chooses B which allows the player to play with 6 lives the game begins and again asks the player for their name, wishes the player the best of luck and advises the hangman game is about to start. It prints the start of the hangman image, with the guess and asks the user to input a letter or word.

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/b35da330-a542-45be-bc53-88563b52d4fb)

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/4f5078e2-7e81-4034-be5a-e8e028a1d975)

<br>

- When the player makes an entry which is outside the range of a letter or word it will print an error.  

<br>

Error printing as result of a number and special character being inputted.

<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/33a7546f-e5be-4185-bc49-ff3fa20c76f4)

<br>

- When an incorrect guess is made the player is advised that they loose a life, prints the amount of lives remaining back to the player and also prints the next part of the hangman.

<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/c86b35b9-375c-4de3-90da-a15860205a55)

<br>

- If the player has used all their lives and failed to guess the word they will be advised that they have 0 lives remaining.  The hangman image with all parts is printed along with You loose and a message advising the game has now ended and prints the correct word.  It then asks the player wheather they would like to play again.  

<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/6d0121a0-d65a-4909-b4d1-13a4560cd674)

<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/8ef2b95d-273c-4e6a-b519-38dd67a0f477)

<br>

- When the player is asked wheather they would like to play again the game expects the player will input either y or n.  If the input is a number, special character or another letter it will print an error.  

<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/54502bbf-51c5-4f36-9de3-92ba3fc6fcf9)

<br>

- When the user inputs y the game will start a new game. 

<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/1bab9dbf-7f9e-45d7-9db5-5002a863e01e)

<br>

- If the player enters n it will print game over
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/f2841582-8f88-4417-91ff-48b5d3ae6025)

<br>

- Finally in my testing i had the random word printed in all my screenshots for the purposes of testing.  When the print(character) statement was removed from the run.py file the output of the random word was a series of underscores with the number of underscores adivising the player how many letter were in the randomly guessed word.

<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/dba2c2ca-8bc8-4108-9172-85567486a98b)

<br>
<br>

| Feature | Acceptance | Pass | Fail |
|:--------|:-------|:-------|:------|
| Run Program Button In Heroku   | When user clicks on button it allows the player to start the game.  | Pass  |  |
| python3 run.py in Gitpod   | When the user enters this command in terminal the game will begin. | Pass |  |
| ASCII Text Welcome To Hangman   | ASCII Text Welcome To Hangman displays when the games runs. | Pass |  |
| Instructions For Game    | Detailed instructions are displayed when the game initializes advising the player on exactly how to play the game. | Pass |  |
| Menu Section    | Allows the user choose one of two options 1 to start playing the game or 2 select a desired level.  | Pass |  |
| Validation On Menu Section | The player can only enter 1 or 2 when they want to choose their option from the menu section any other input the game will present the player with an error.  | Pass |  |
| Menu Option 1 Start Playing The Game    | When the player chooses option 1 the game will start. | Pass |  |
| Menu Option 2 gives two levels   | When the user chooses option 2 they will be presented with A to play with 4 lives or B to play with 6 lives. | Pass |  |
| Validation On Choosing levels   | The game will not accept anything other than A or B as an input.  | Pass |  |
| Level A Initialisation   | When A is inputted the game starts with 4 lives. | Pass |  |
| Level B Initialisation    | When B is inputted the game starts with 6 lives. | Pass |  |
| Validation of inputs at each level   | When the player makes a guess at each level the game will only accept a letter or word it will not accepts numbers or special characters. | Pass |  |
| Displaying No of Lives and Hangman Stages    | At each level if the user makes an incorrect guess the number of lives reamining is displayed back to the player and the hangman is displayed at the corresponding stage to the number of lives remaining. | Pass |  |
| Successfull Guesses    | When the user makes a successfull guess the player is notified of same and if the player has guessed the word they are also notified of same. | Pass |  |
| Unsuccessfull Guesses    | When the player guess in unsuccessful the player is again notified of same and if the player fails to guess the word the player is notified of same and advised that there is no more live reminaing to guess the word and game is over.   | Pass |  |
| Play Again    | The player is asked at the end of each game wheather successful or unsuccessfull whether they would like to play again. | Pass |  |
| Play Again Validation    | The game will only accept y if the player wants to play again and no if they do not want to play.  The game will print an error if another letter, number or special character is entered.  | Pass |  |

<br>
<br>

### Validation on CI Python Linter

The code for all files named below was run on the CI Python Linter - https://pep8ci.herokuapp.com/

<br>
run.py file 
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/090a4468-f702-49fc-9f25-27e906bd42cd)

<br>
score.py file
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/0a8612db-5849-4e7f-9244-3db12b99d54b)

<br>
wordlists.py
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/c136048f-270e-441e-ba74-c5fb72d36e84)

<br>
When flake8 was run in the terminal no errors were provided 
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/7d14b1e7-a889-4b5c-80e7-b96dbbe23c12)

<br>
Also tested the app on the following browsers with no issues:
- Microsoft Edge

<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/d258b891-0995-44e3-9ef9-a001a1d4a5aa)

<br>

- FireFox

<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/e87fd935-7e51-4a6f-b9ec-a2f9eb0dfa89)

