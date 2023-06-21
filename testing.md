[Link Back To Main Readme Document](README.md)

## Testing 
<br>

### Testing of Developer / Owner Goals and Player / User Goals

| Goals | Acceptance | Pass | Fail |
|:--------|:-------|:-------|:------|
| Developer / Owner Goals   |  |  |  |
| 1 Offer entertainment to the player wo want to play the game   | The hangman game has a very user friendly interface which make the game enjoyable and fun to play | Pass |  |
| 2 It should have clear instructions displayed to player    | When the Hangman game commences it displays a full list of instructions to the player which are very clear and detailed | Pass |  |
| 3 To allow the user interact with the game by adding inputs to questions and guesses for words.    | The hangman game allows the player to start the game or choose a level at the start.  It also allows the player to enter a guess in letter or word format  | Pass |  |
<br>

| Player / User Goals    |  |  |  |
| 1 The game should be easy to play    | The interface that the hangman game is very easy to use and engage with as a player  | Pass | xxx |
| 2 It should have clear instructions displayed to the player  | When the game commences it displays a full set of instructions to the user so that they know exactly how to play the game.   | Pass | xxx |
| 3 The game should be fun and engaging   | The game allows the player to choose a level and also allows the player to guess either by letter or word and also allows the user to test their guessing ability with different levels which makes it fun and engaging.  | Pass  |  |
| 4 Easy navigation throughout the game  | The hangman game is very easy to navigate. It promptss the user for their input at every step making it very easy to naviage for the user.  | Pass |  |
| 5 Be challenging by providing different player levels   | In the menu section of the game when the player chooses 2 it splits into A and B where if the player chooses A they play with 4 lives and B plays with 6 lives | Pass |  |

### Testing of Features and Validation
- Start Game
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/abdd8f4a-021c-4468-b328-d92ed81cf362)  UPDATED SCREENSHOT 
When the player clicks on Run Program on Heroku it runs the game and the player can see the Welcome banner "Welcome To Hangman".  It then displays a list of instructions which explains exactly how to play the game.  In the Menu section the player can choose 1 to start playing the hangman game or 2 to choose a desired level. 
<br>
- In Gitpod the player will type "python3 run.py" in the terminal and this will run the program and displays the exact details like when the program in run in Heroku (see above). UPDATE SCREENSHOT 
- The information displayed and steps are the same in Heroku and Gitpod from this point onwards.  
- Validation 
If the player inputs a different no, letter  or special character the Hangman Program will print an error. 
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/2eb1ed35-3b12-4398-b460-82a6243768a6)
- When the player chooses the 1 in the Menu Section the game will begin where it asks the player for their name and wishes them the best of luck.  (For the purposes of testing i have the random word printed to the terminal so i validate the game this will not be printed in the actual game.) The start of the hangman displays and underscores are printed to represent the hidden word.  The player is then asked to enter a letter or word  