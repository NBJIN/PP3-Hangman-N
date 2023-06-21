[Link Back To Main Readme Document](README.md)

## Testing 
<br>

### Testing of Developer / Owner Goals and Player / User Goals

| Goals | Acceptance | Pass | Fail |
|:--------|:-------|:-------|:------|
| Developer / Owner Goals   |  |  |  |
| 1.  Offer entertainment to the player wo want to play the game   | The hangman game has a very user friendly interface which make the game enjoyable and fun to play | Pass |  |
| 2.  It should have clear instructions displayed to player    | When the Hangman game commences it displays a full list of instructions to the player which are very clear and detailed | Pass |  |
| 3.  To allow the user interact with the game by adding inputs to questions and guesses for words.    | The hangman game allows the player to start the game or choose a level at the start.  It also allows the player to enter a guess in letter or word format  | Pass |  |
| Player / User Goals    |  |  |  |
| 1.  The game should be easy to play    | The interface that the hangman game is very easy to use and engage with as a player  | Pass | xxx |
| 2.  It should have clear instructions displayed to the player  | When the game commences it displays a full set of instructions to the user so that they know exactly how to play the game.   | Pass | xxx |
| 3.  The game should be fun and engaging   | The game allows the player to choose a level and also allows the player to guess either by letter or word and also allows the user to test their guessing ability with different levels which makes it fun and engaging.  | Pass  |  |
| 4.  Easy navigation throughout the game  | The hangman game is very easy to navigate. It promptss the user for their input at every step making it very easy to naviage for the user.  | Pass |  |
| 5.  Be challenging by providing different player levels   | In the menu section of the game when the player chooses 2 it splits into A and B where if the player chooses A they play with 4 lives and B plays with 6 lives | Pass |  |

### Testing of Features and Validation
- Start Game
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/abdd8f4a-021c-4468-b328-d92ed81cf362)  UPDATED SCREENSHOT 
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
- Validation 
If the player inputs a different no, letter  or special character the Hangman Program will print an error. 
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/2eb1ed35-3b12-4398-b460-82a6243768a6)
- When the player chooses the 1 in the Menu Section the game will begin where it asks the player for their name and wishes them the best of luck.  (For the purposes of testing i have the random word printed to the terminal so i validate the game this will not be printed in the actual game.) The start of the hangman displays and underscores are printed to represent the hidden word.  The player is then asked to enter a letter or word.
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/addfeca7-2af9-4e2d-a269-1438bb551142) 
 - If the player doesn not enter a letter or word a message will print back to the player that the Hangman game only accepts letters or words, guess is incorrect and it deducts a life.
 <br> 
 Tested with numbers
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/4bdc2311-4574-49c8-aa58-d3b6545e0f6a)
 <br>
 Tested with special characters
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/a62d9df0-d046-4d6e-b556-4ead043e440b)
 - When the player enters a correct guess a message of congratulations is displayed back to the player and asks the player to guess another word.  
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/0a626e1a-a184-4526-ade3-eb8b7d0c4ba0)
 - If the playeer guesses all letters/word correctly ASCII text of "You Win" is displayed back to the user along with a message that congratulates the user and displays the correct word again.  The player is also asked wheather they would like to play the game again.  
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/dc4af21e-1500-4744-a10b-96bd676bee3e)
 - Should the player enter a differnt character besides y or n to play the game again it will print an error.
 <br>
 Error which appears when different letters, numbers and special characters are entered.
 <br>
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/7d04db2b-15ef-4758-a5cf-3737ac18e954)
 - When the player enters y it will start the new game 
 <br>
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/52733a79-2dde-4bd6-a270-1e039f904078)
 <br>
 - When the player enters n it will print game over
 <br>
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/a8b0239d-255e-4d75-bc80-2fdb090e922f)
 <br>
 - When the player enters 2 to choose the desired level on the menu section 