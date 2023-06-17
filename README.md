###### insert picture of project 

# Hangman

<p align="justify" >
This Hangman game is a Python terminal guessing game where the user is playing against the computer in which it randomly chooses a word.  The player ties to guess the word by suggesting letter or even the word itself.  The word to guess is represented by a row of dashes with each dash representing a letter.  The player gets a number of lives in order to guess the letters or word.  If the player enter too many failed attempts the 
game is lost.  

The game can be visited at PUT IN FINAL DEPLOYED LINK
The respository can be vistited at PUT IN FINAL LINK HERE 
</p>
<br>

## Table of Contents
#
1. [ How To Play](#how-to-play)

2. [ Target Audience](#target-audience)

3. [ UX Planning Stage](#ux-planning-stage)

    a) [ Developer Owner Goals](#developer-owner-goals)<br>
    b) [ Player User Goals](#player-user-goals)<br>
    c) [ Flowchart](#flowchart)    

4. [ Features](#Features)
#



## How To Play 
#
The idea of the Hangman Game is to get the hidden word so in order to play the game the player goes through the following steps On Gitpod. 

1) Enter "python3 run.py" command in the terminal 
2) This will initiate the Hangman game where the welcome note is displayed followed
by the instructions and then the Menu.
3) In the Menu section the player is given two options where 1 there can start playing the Hangman game or 2 choose the desired level they want to play at.
4) If the player chooses 1 they will be asked for their name.
5) Then the program will print Best of luck with the name of the player.
6) The Hangman program then advises the player that the game is going to start. 
7) Next the start of the hangman image is displayed and the underscores for the word is also displayed.  
8) The player is then asked to guess a letter or character.
9) If the letter or word is correct the player will be advised of same. 
10) The letter or character guessed will be displayed instead of the underscores.  
11) If the word is not complete the player will be asked to guess another letter or 
character.  
12) If the players guess is incorrect a message is displayed to the user saying their guess is not in the character, they loose a life and it prints the number of lives left to the terminal. It also prints the hangman image with the next body part filled in. 
13) If the user looses all lives the program advises the player that the guess is incorrect with 0 lives remaining. 
14) It also prints the hangman complete with all parts aswell as ASCII text of You Loose.  
15) It advises the player that the game has now ended.  It confirms the unguessed word and displays to the player please try again.  
16) It also asks the user if they would like to play again whereby the user enter y for yes and n for no.
17) If the player chooses y the game starts all over again.  
18) If the player guesses all letter or word correctly a message is displayed to the user in ASCII text You Win.  
19) It also displays congratulations you guessed the character and then the name of the character and confirms to the player that they have won the game.  
20) It then asks the player if the would like to play again and the user enters y for yes and n for no.  
21) When the user starts the game and chooses option 2 in the menu section to choose their desired level it will display 2 options back to the user where they can A choose a a level which has 4 lives or B which has 6 lives. 
22) The Hangman program will then ask the user for their name and the game starts all over again from point 5 above.  
#

## Target Audience

Hangman is a game for everyone: 
- Adults who just want a break from computer work and want to play a game for fun or to do something deifferent for 10 minutes. 
- Kids for fund or to imporve problem solving, concentration, spelling, pronunciation and vocabulary skills.
- Teachers can use with students.  

#
## UX - Planning Stage

- Developer / Owner Goals
    - To offer entertainment to the player who wants to play the game
    - To provide the user with clear instruction and information. 
    - To allow the user interact with the game by adding inputs to questions and guesses for characters.  
    <br>
    <br>

- Player / User Goals
    - The game should be easy to play 
    - It should have clear instructions displayed to player
    - The game should be fun and engaging 
    - Easy navigation throughout the game 
    - Be challenging by providing different player levels
    <br>
    <br>


- Flowchart 
In brainstroming and designing stage for this game i put togeather a flowchart of the steps that would be involved in playing the game. From this you can see that once the game is started it mapps out each step that the player will take. It shows where the player needs to interact with the game by inputting their name, wheather they want to start the game straight away or to choose a desired level.  Also the main part of the players input is guessing the letters or characters.  The flowchart shows the path the game will take if the player guess was successfull and where it was unsuccessfull.  The flowchart also points out where the program itself directs the player by providing the random word in which the player has to guess.  

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/877e936d-b02a-4423-99c2-70f1391b653e)


# 
## Features 
* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!