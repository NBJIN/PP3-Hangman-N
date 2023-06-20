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

4. [ Features](#features)

5. [ Testing](#testing)

6. [ Technologies Used](#technologies-used)

7. [ Bugs](#bugs)

8. [ Deployment](#deployment)

9. [ Credits](#credits)
#



## 1. How To Play<a name="how-to-play"></a>
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
<br>
<br>

When the player wishes to play the game on Heroku it similar steps to the above but in the Heroku Link the player clicks on RUN PROGRAM which will initiate the Hangman game and the steps can be followed as per point 2 above when running it it Gitpod.

<br>

#

## 2 Target Audience<a name="target-audience"></a>

Hangman is a game for everyone: 
- Adults who just want a break from computer work and want to play a game for fun or to do something deifferent for 10 minutes. 
- Kids for fund or to imporve problem solving, concentration, spelling, pronunciation and vocabulary skills.
- Teachers can use with students.  

#
## 3 UX - Planning Stage<a name="ux-planning-stage"></a>

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
## 4 Features<a name="features"></a>

### Existing Features
- Start Game <br>
On Heroku the player clicks on "Run Program" 
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/abdd8f4a-021c-4468-b328-d92ed81cf362) 
<br>
In Gitpod the player will type "python3 run.py" in the terminal
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/db017b2b-c95c-41b5-8c5b-0fc9cc2b5786)

 - Every step after this will be the same on Heroku and Gitpod

 - Welcome Screen is displayed to the Player which displays "Welcome To Hangman" in ASCII text.  A picture of the hangman is also displayed along with the Instruction for the player.  This also includes a Menu section where the player can 1 choose to start playing hangman or 2 choose the desired level.  
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/fcf94e26-8e79-4e6b-a0b0-86af6dad2ed7)
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/34b2cc5a-782c-4796-a866-901937c0b440)

 - If the player chooses option 1 to start playing the game they will be asked for their name, wished the best of luck and advised that the game is about to start in which it will display the start of the hangman image without any parts.  (I have a print statement in my code at present just to show the word that is randomly selected by the Hangman program).  The player is then requested to gues a letter or character.  
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/bccb6a5d-7495-444b-add0-0c06b714334f)

- If the player input a correct guess a message is displayed confirming the guess is correct and the letter or word is printed in the underlined spaces provided. If the word is not fully guessed the player will be asked to guess a letter or character again.   
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/5b607e38-f229-4877-8a21-8276e38cdcb5)

- If the player makes an incorrect guess the player is advised that it is incorrect, a life is lost and the number of remaining lives is printed. The hangman is also printed with the parts added.  If the player has lives remaining they will be asked to make another guess.  
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/5baab917-e512-4110-a1cc-872f1b18ba07)

- If the player input somthing other than a letter or character (word) it will advise the player of same.  
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/9e767a2f-8661-462b-9930-ee614a49a14d)

- Should a player guess a letter twice they are notified of same.
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/dc738934-956b-43ae-932e-af19795bafef)

- When the player corectly guesses all letters or the character (word) ASCII text is displayed saying You Win and a note to say Congratulations you guess the character (word) you have won this game.  After this the player is asked wheather they would like to play again by inputting y for yes and n for no. If the player chooses y then the game starts all over again.  
![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/d5b739c6-1a2c-4bca-9c50-baf90e9ba09b)

- If a player looses all lives without guessing the word You Loose is displayed in ASCII text and a message is displayed to the player advising the game has ended and prints the correct word.  The player is also asked if they would like to play again by entering y for yes and n for no. 
 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/ed95b0ea-ded3-44e3-bdbe-327efbcf2104)


- If the user chooses option 2 from the menu section they will then be asked to choose a level.  Should the player choose level A they will play with 4 lives.  If B is chosen the player will be given 6 lives to play with.  

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/e25a7a7b-546c-41f7-b926-41621190f1fc)

- When the player chooses a level the game starts requested the players name and wishing the player the best of luck and notification that the Hangman game is about to start.  The start of the hangman is displayed and the player is requested to make a guess and the game begins.  (Print statement added just to show the word to show the word randomly selected by the hangman program). 

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/20957e6c-bcc7-4c8b-b5f5-179bec013af1)



### Future Features
- Color Scheme for example You Won Screen displayed in green text and You Loose displayed in red text.  
- 	Record score of a number of players where they play against each other and record the best of say 5 games by connecting same to google spreadsheet which will record these results.  

#
## 5 Testing<a name="testing"></a>

#
<br>

### Please refer to testing.md file for full breakdown of testing that was carried out.  

[Testing](testing.md)

# 

## 6 Technologies Used<a name="technologies-used"></a>

### Languages
- 	Python - https://en.wikipedia.org/wiki/Python_(programming_language)
<br>

### Libraries
- Random to select a random word from the wordlist
<br>

### Other
- Code Institute full template for python used to build project - https://learn.codeinstitute.net/
- Git used for version control by using the Gitpod terminal to commit to Git and push to GitHub - https://www.gitpod.io/ - https://www.github.com
- GitHub is used to store the projects code after being pushed from Gitpod
- Heroku used to host Hangman game. - https://id.heroku.com/login
- words.txt - A list of randomly generated words to be used to select a word to play, taken from (https://www.randomlists.com/random-words). CHECK THIS
- ASCII Art Generator - http://patorjk.com/software/taag/#p=display&f=Shadow&t=Welcome%20To%20Hangman 

#


## 7 Bugs<a name="bugs"></a>

#

## 8 Deployment<a name="deployment"></a>
The project was deployed using Code Institutes mock terminal for Heroku.
Steps to deploy:
- Fork or clone this repository.
- Ensure the Procfile is in place in your gitpod workspace and ensure all work is committed and pushed to github
- Then go to Heroku and login - https://id.heroku.com/login.  If you don’t have an account click on signup on this link 
- Once logged in and on the main page select “New” at the top of page 
- Select "Create new app".
- Name the new app and click "Create new app".
- In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list).
- Whilst still in "Settings", click "Reveal Config Vars" and input the following. KEY: PORT, VALUE: 8000. Nothing else is needed here as this project does not have any sensitive files.
- Click on "Deploy" and select your deploy method and repository.
- Click "Connect" on selected repository.
- Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.
- Heroku will now deploy the site.
#
	
## 9 Credits<a name="credits"></a>
- Code Institute LMS for notes and videos and also the template provided for the project.  https://learn.codeinstitute.net/dashboard
- Random Word Generator - to generate a random list of 500 words for the game.
- The following python tutorials for inspiration on how to build a hang man game.  
https://youtu.be/m4nEnsavl6w (Kite)
https://youtu.be/cJJTnI22IF8 (Kylie Ying)
- ASCII Art Generator http://patorjk.com/software/taag/#p=display&f=Shadow&t=Welcome%20To%20Hangman - for creating word art for welcome, you won and game over screens.
- Slack for researching and troubleshooting problems/issues with code - https://slack.com/intl/en-ie/
- Slack project-portfolio-3 channel for research, guidance on structure, layout and design.  
- Python All-In-One for dummies 2nd Edition by John C. Shovic and Alan Simpson
- Stackoverflow used to research some issues - https://stackoverflow.com/
- Cohort Facilitator at CI for all their help and guidance
- Cohort Lead and class for all their help and support. 
- Tutor Assistance at CI who guided me in resolving bugs and issues in code
- Student Care at CI for all their Support and guidance
- My Mentor for excellent ideas, guidance and support.  

#
#
#















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