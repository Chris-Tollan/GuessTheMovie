# Guess the Movie

![image](https://github.com/Chris-Tollan/GuessTheMovie/assets/134441833/88f36c5f-18b7-413c-905f-afeff1460fff)

Link to Deployed Site - https://guess-the-movie-5e4107e9e431.herokuapp.com/

## Aim

Guess The Movie is a word unscrambler game. In this command line application, the user will be presented with a Movie title which has been scrambled to make it unreadable, to progress through the game the user must correctly unscramble the Movie title.

When first run, the user will enter a username...points are gained for correct answers. The users final score will be added to a leaderboard if it is within the top score amongst other users. 

## User Experience (UX)

### Goals

- Design annd build an interactive application where the user will be provided a movie title, the letters of which have been scrambled to make the title unreadable. The user will be required to unscramble the letters and guess the correct Movie title to progress through the game.
- Build the application using only Python and run it in a Command Line Interface.
- Deploy the application using Heroku.
- The application must recognise errors in user input and provide clear feedback to the user so they can easily navigate the application.
- The application will be easy to navigate and understand.
- The application will be fun to play, however challenging enough to keep the user invested.
- The application will have a scoring system and leaderboard so the user can return to beat previous scores or compete against other users. An API will be utilised to store the username and score of the user using Google Sheets.
 
## User Sories

### First Time Visitor Goals

1. As a First Time Visitor, I want to easily understand the main purpose of the application and intuitively understand how to navigate it.
2. As a First Time Visitor, I want to be able to progress through the application at a speed that matches my ability.
3. As a First Time Visitor, I want to be able to view my score and also see how it compares against the other users by viewing a leaderboard.

### Returning and Frequent Visitor Goals

1. As a Returning Visitor, I want to have a different experience each time I play by not being present with the same set of Movie titles every time.
2. As a Returning Visitor, I want to be able to increase the difficulty in order to further challenge myself.
3. As a Returning Visitor, I want to improve my score and where I feature on the leaderboard.

## Planning

### Logic Flowchart
    
- The below flowchart was created using Lucid Charts and it shows:
  
    - The navigation around the application and how it will allow for a user friendly and easy to navigate game for the user.
    - Anything input by the user must pass validation before the game can progress.

![Flowcharts](https://github.com/Chris-Tollan/GuessTheMovie/assets/134441833/6350d7c9-3503-4ba0-b7ba-1a5848004f5b)
            
## Features

### Welcome Screen

- When the application is run a Welcome Screen will be displayed which will display a greetings message and present the user with the option to enter their name.

![image](https://github.com/Chris-Tollan/GuessTheMovie/assets/134441833/54d88cda-12bc-4ac3-b4f1-fbbab36b0bc7)

### Instructions

- The user will then be provided with the instructions on how to naviagte through the application and play the game.
 
![image](https://github.com/Chris-Tollan/GuessTheMovie/assets/134441833/4d0b117f-8c1b-4c98-b66d-6cd64829e8cd)

### Leaderboard

- The leaderboard, referenced in the game as "Walk of Fame" which is a ploy on the famous Hollywood Walk of Fame, will feature the top ten scores achieved by users.

![image](https://github.com/Chris-Tollan/GuessTheMovie/assets/134441833/07ed8e92-bfbe-4306-b71c-e16b3d3338a1)

### Game

- The user will be presented with 10 different movie titles, one at a time, the letters of which are shuffled at random
 
![image](https://github.com/Chris-Tollan/GuessTheMovie/assets/134441833/53b96b6d-908b-488c-9b7b-1c5709774729)
 
### Game Over

- On completetion of the game the user will be provided with their final score which will be updated to the leaderboard. The leaderboard will then display followed by the user being presented with the option to return to the welcome screen.
 
![image](https://github.com/Chris-Tollan/GuessTheMovie/assets/134441833/a0aa388c-b903-4c50-b7dc-33504fc22333)

![image](https://github.com/Chris-Tollan/GuessTheMovie/assets/134441833/3832a137-1c11-4b39-a7c6-73b984204946)

### Features Still to Implement

- Going forward with this project and as my skillbase expand there are a number of features I would love to implement in this project which I feel would improve the users experience and overal game play:
  
    - Along with a username which could be validated in order to be 100% unique to them, the user could be asks to create a password so only they can access and play with this username.
    - Instead of using a list of movie titles within the code itself and API could be implemented to randomly select movie titles, this would allow for a different user experience everytime they played.
    - Different difficulty levels could be implemented to make the game easier or harder based on the users ability and knowledge level. 

## Technologies Used

### Languages Used

-   Python
    The following libraries were used within Python
    - Logging
    - os
    - Random
    - Path
    - gspread
    - requests
    - pyfiglet
    - colorama
    - warnings   

### Tools and Technologies

- Lucid Charts - Used to develop a flow chart for the logic flow for this project
- Github - Used to story the reposiitory for this project
- Codeanywhere - Used to write, develop, preview the code and also to push it to GitHub
- Git - Used for version control
- Heroku -  Used to deploy the project
- CI Python Linter - Used to test and validate the code for this project

## Testing

- The project for continuously tested throughout the development of the project by the developer.
- The deployed project has also been testing by the developer and his friends and family in order for a broad level of feedback to be received for each users experience.
- The code for the project has been validated through the CI Python Linter as per the following image:

![image](https://github.com/Chris-Tollan/GuessTheMovie/assets/134441833/4073fd00-088f-43ce-a823-cea3697e4ef9)

- No error messages have been displayed via the linter.

### Known Bugs

- Following deployment of this project no bugs have been discovered.

## Deployment

This website has been deployed using Heroku.

Instructions to deploy using Heroku:

1 - While in Heroku, navigate to dashboard and then click on the new button in the top right corner choosing: create new app.

2 - Input a name for your app (this name will need to be unique) and choose the correct region for where you are located. Click create app.

3 - Your app has been created, now click on the settings tab.

4 - Click reveal config vars to add any keys the application will need. For this project I added the api credentials for my spreadsheet to a key of CREDS and a value of 8000 to a key of PORT.

5 - Click add buildpack to install any interdependecies needed. For this project I installed 'python' and 'nodejs'.

6 - Click on deploy tab. Select deploy method, in this case Git Hub. Confirm connection to git hub by searching for the correct repository and then connecting to it.

7 - To manually deploy project click 'Deploy Branch'. Once built a message will appear saying: Your app was successfully deployed. Click the view button to view the deployed page making a note of it's url.

## Credits

### Code

- Throughout this project I have researched a number of tutorials and viewed project of a similar nature. From doing this I found the following of partiicular help:
    - Make a word unscrambler/spelling game in Python, YouTube Tutorial by Pythonology - (https://www.youtube.com/watch?v=-Rz4fM-J0CY)
        - I used the code from this tutorial and edited it where neccesary to create the the begin_game_play function for my project.
     
    - My fellow Code Institute student Helen Murugan created a word scrambler game which can be accessed via this link (https://github.com/helenmurugan/scrambled-tech/tree/main)
        - I used the code from Helens project to assist me with creating my leaderboard function and in particular uploading the current users score to the leaderboard. 

### Content


### Acknowledgements

-   My Mentor Narender Singh for his continuous helpful support and feedback.

-   Tutor support at Code Institute for their support.

-   Fellow members of the Slack community for their continuous help, feedback and guidance.

-   Helen Murugan for granting me permission to view her leaderboard code in order to create mine for this project.
