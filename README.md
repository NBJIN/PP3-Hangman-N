![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/2d0d4ad6-db94-4c32-b7c8-ef847eb304f3)

# Hangman

<p align="justify" >
This Hangman game is a Python terminal guessing game where the user is playing against the Hangman program in which it randomly chooses a word.  The player tries to guess the word by suggesting a letter or even the word itself.  The word to guess is represented by a row of underscores with each underscore representing a letter.  The player gets a number of lives in order to guess the letters or word.  If the player enters too many failed attempts the game is lost.  

The game can be visited at PUT IN FINAL DEPLOYED LINK
<br>
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
The idea of the Hangman Game is to get the hidden word.  In order to play the game the player goes through the following steps. 

1) Click on Run Program on Heroku or Enter "python3 run.py" command in the gitpod terminal.  
2) This will initiate the Hangman game where the welcome note is displayed followed by the instructions and then the Menu.
3) In the Menu section the player is given two options where 1 the player can start playing the Hangman game or 2 choose the desired level they want to play at.
4) If the player chooses 1 they will be asked for their name.
5) Then the program will print Best of luck with the name of the player.
6) The Hangman program then advises the player that the game is going to start. 
7) Next the start of the hangman image is displayed and the underscores for the word is also displayed.  
8) The player is then asked to guess a letter or word.
9) If the letter or word is correct the player will be advised of same. 
10) The letter or word guessed will be displayed instead of the underscores.  
11) If the word is not complete the player will be asked to guess another letter or a word.  
12) If the players guess is incorrect a message is displayed to the user saying their guess is not in the word, they loose a life and it prints the number of lives left to the terminal. It also prints the hangman image with the next body part filled in. 
13) If the user looses all lives the program advises the player that the guess is incorrect with 0 lives remaining. 
14) It also prints the hangman completed with all parts aswell as ASCII text of You Loose.  
15) It advises the player that the game has now ended.  It confirms the unguessed word and displays it to the player.  
16) It also asks the user if they would like to play again whereby the user enter y for yes and n for no.
17) If the player chooses y the game starts all over again.  
18) If the player guesses all letters or the word correctly a message is displayed to the user in ASCII text You Win.  
19) It also displays congratulations you guessed the word and then the name of the character and confirms to the player that they have won the game.  
20) It then asks the player if the would like to play again and the user enters y for yes and n for no.  
21) When the user starts the game and chooses option 2 in the menu section to choose their desired level it will display 2 options back to the user where they can A choose to play with 4 lives or B play with 6 lives. 
22) The Hangman program will then ask the user for their name and the game starts all over again from point 5 above. 
<br>
<br>

#

## 2 Target Audience<a name="target-audience"></a>

Hangman is a game for everyone: 
- Adults who just want a break from computer work and want to play a game for fun or to do something deifferent for 10 minutes. 
- Kids for fun or to imporve problem solving, concentration, spelling, pronunciation and vocabulary skills.
- Teachers can use with students.  
<br>
<br>

#

## 3 UX - Planning Stage<a name="ux-planning-stage"></a>

- Developer / Owner Goals
    - To offer entertainment to the player who wants to play the game.
    - To provide the user with clear instruction and information. 
    - To allow the user interact with the game by adding inputs to questions and guesses for words.  
    <br>
    <br>

- Player / User Goals
    - The game should be easy to play. 
    - It should have clear instructions displayed to player.
    - The game should be fun and engaging. 
    - Easy navigation throughout the game. 
    - Be challenging by providing different player levels.
    <br>
    <br>


- Flowchart 
<p align="justify">In the brainstroming and designing stage for this game i put togeather a flowchart of the steps that would be involved in playing the game. From this you can see that once the game is started it maps out each step that the player will take. It shows where the player needs to interact with the game by inputting their name, wheather they want to start the game straight away or to choose a desired level.  Also the main part of the players input is guessing the letters or word.  The flowchart shows the path the game will take if the player guess was successfull and where it was unsuccessfull.  The flowchart also points out where the program itself directs the player by providing the random word in which the player has to guess.</p>  
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/d57008b7-456f-4fa2-a56a-ee95e02986d6)
<br>
<br>

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

 - Welcome Screen is displayed to the player which displays "Welcome To Hangman" in ASCII text.  A picture of the hangman is also displayed along with the instructions for the player.  This also includes a Menu section where the player can 1 choose to start playing hangman or 2 choose the desired level.  

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/a8212703-c927-4940-af6f-cc79d0931c5b)
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/f8a82527-4800-47fd-95ea-55cc0df97d67)
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/8e4ce074-520c-4ede-ac68-83946cf18af7)
<br>

 - If the player chooses option 1 to start playing the game they will be asked for their name, wished the best of luck and advised that the game is about to start in which it will display the start of the hangman image without any parts.  (I have a print statement in my code at present for testing purposes just to show the word that is randomly selected by the Hangman program).  The player is then requested to guess a letter or word. 

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/addfeca7-2af9-4e2d-a269-1438bb551142) 

- If the player input a correct guess a message is displayed confirming the guess is correct and the letter or word is printed in the underlined spaces provided. If the word is not fully guessed the player will be asked to guess a letter or character again.   

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/0a626e1a-a184-4526-ade3-eb8b7d0c4ba0)

- If the player makes an incorrect guess the player is advised that it is incorrect, a life is lost and the number of remaining lives is printed. The hangman is also printed with the parts added.  If the player has lives remaining they will be asked to make another guess.

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/5baab917-e512-4110-a1cc-872f1b18ba07)

- If the player inputs somthing other than a letter or word it will advise the player of same.  

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/9e767a2f-8661-462b-9930-ee614a49a14d)

- Should a player guess a letter twice they are notified of same.

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/dc738934-956b-43ae-932e-af19795bafef)

- When the player corectly guesses all letters or the word ASCII text is displayed saying you win and a note to say congratulations you guess the word you have won this game.  After this the player is asked wheather they would like to play again by inputting y for yes and n for no. If the player chooses y then the game starts all over again. 

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/d5b739c6-1a2c-4bca-9c50-baf90e9ba09b)

- If a player looses all lives without guessing the word You Loose is displayed in ASCII text and a message is displayed to the player advising the game has ended and prints the correct word.  The player is also asked if they would like to play again by entering y for yes and n for no.

 ![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/ed95b0ea-ded3-44e3-bdbe-327efbcf2104)


- If the user chooses option 2 from the menu section they will then be asked if they want to play with 4 lives in choosing A or 6 lives in choosing B.  

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/adee0a9a-82be-4ced-b856-c17ea0eae755)

- When the player chooses a level the game starts requests the players name and wishes the player the best of luck and notification that the Hangman game is about to start.  The start of the hangman is displayed and the player is requested to make a guess and the game begins.  (Print statements added just to show the random word for testing purposes selected by the hangman program). 

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/9476919f-1588-4aa6-a17d-6c1d173ac254)



### Future Features
- Color Scheme for example You Won Screen displayed in green text and You Loose displayed in red text.  
- 	Record score of a number of players where they play against each other and record the best of say 5 games by connecting same to google spreadsheet which will record these results.  
<br>
<br>

#

## 5 Testing<a name="testing"></a>
<br>

### Please refer to testing.md file for full breakdown of testing that was carried out.  

[Testing](testing.md)

<br>
<br>

# 

## 6 Technologies Used<a name="technologies-used"></a>

### Languages
- 	Python - https://en.wikipedia.org/wiki/Python_(programming_language)
<br>

### Libraries
- Random to select a random word from the wordlist.
- Time provides various function in relation to time.
- OS provides a way in which to interact with the system.
<br>

### Other
- Code Institute full template for python used to build project - https://learn.codeinstitute.net/
- Git used for version control by using the Gitpod to write code and the terminal to commit to Git and push to GitHub - https://www.gitpod.io/ - https://www.github.com
- GitHub is used to store the projects code after being pushed from Gitpod - https://www.github.com
- Heroku used to host Hangman game. - https://id.heroku.com/login
- wordlists.py - A list of randomly generated words to be used to select a word to play, random list of words taken from (https://www.randomlists.com/)
- ASCII Art Generator - http://patorjk.com/software/taag/#p=display&f=Shadow&t=Welcome%20To%20Hangman 
- The flowchart for this project was generated using the following website - https://www.smartdraw.com/
- Responsiveness image was generated through - https://techsini.com/multi-mockup/index.php
<br>
<br>

#

## 7 Bugs<a name="bugs"></a>

- When writing my code i had over 100 problems in the terminal in relation to invalid escape sequence and anomalous backslash in string. These were all coming from the score.py specifically from the ASCII text that i had inputted for WELCOME, WIN, LOOSE and GAME_OVER.  Below is just a sample of the errors. While researching projects on peer code review on slack came across some details in relation to this issue.  
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/302ce637-401a-4a9d-95f9-28c21b8ff09e)
<br>
In order to fix the above everywhere there was a backslash in my score.py ASCII text code I entered a corresponding backslash and this removed all of these errors.  
<br>
- I also had a number of problems in relation to gitpod.yml file. See screenshot below for errors.

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/a261026f-97a1-4f8e-a238-722157ea5c61)
<br>
When i hovered over the above problems it gave the following fixes:
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/89ab7a94-ad8e-4f0d-8879-7e8b39bfcd7f)
<br>
I added all the above extension to the gitpod.yml file and it removed all the problems from the terminal. 
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/66427350-e7c7-41a0-8c6d-6ff00dbc9bd6)
<br>
The following was the output when i added all extensions to gitpod.yml
<br>

![image](https://github.com/NBJIN/PP3-Hangman-N/assets/106515976/0769b5db-94d3-4335-8ac8-b75625785eb6)

<br>
While implementing this project came across a lot of errors in relation to line too long and trailing white spaces but all have been addressed.  
<br>

### Known Bugs

Not on all occasions but sometimes the random generator will generate the same words to be guessed but other than that there are no other bugs.  
<br>
<br>

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
<br>
<br>

#
	
## 9 Credits<a name="credits"></a>
- Code Institute LMS for notes and videos and also the template provided for the project.  https://learn.codeinstitute.net/dashboard
- Random Word Generator - to generate a random list of 500 words for the game. - (https://www.randomlists.com/)
- The following python tutorials for inspiration on how to build a hang man game.  
https://youtu.be/m4nEnsavl6w (Kite)
https://youtu.be/cJJTnI22IF8 (Kylie Ying)
- ASCII Art Generator http://patorjk.com/software/taag/#p=display&f=Shadow&t=Welcome%20To%20Hangman - for creating word art for welcome, you won, you loose and game over screens.
- Slack for researching and troubleshooting problems/issues with code - https://slack.com/intl/en-ie/
- Slack project-portfolio-3 channel for research, guidance on structure, layout and design.  
- Python All-In-One for dummies 2nd Edition by John C. Shovic and Alan Simpson
- Stackoverflow used to research some issues - https://stackoverflow.com/
- Cohort Facilitator at CI for all their help and guidance
- Cohort Lead and class for all their help and support. 
- Tutor Assistance at CI who guided me in resolving bugs and issues in code
- Student Care at CI for all their Support and guidance
- My Mentor for excellent ideas, guidance and support.  
