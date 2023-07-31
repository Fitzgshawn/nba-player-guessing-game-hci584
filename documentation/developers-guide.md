## Overview
This app will generate a random player from a list of current NBA players. The list of NBA players comes from NBA.com, more specifically their stats page. The website gathers statistics from every active player from the 2022-2023 NBA season. All of the table data is scraped directly from the NBA.com site, and placed into a table, saved as a .csv file. The GUI requests a random NBA player for the game to begin, and highlights the columns of the table that need to be pulled in for the game to begin, such as player's name, points per game, rebounds per game, assists per game, age, and the players team during the 2022-2023 NBA season.

The app will provide the points per game for the random player and the user will be prompted to make their first guess. The user will make an initial guess by typing into an input field and submitting, If the user is incorrect, the app will provide them with a hint.
As the user continues to guess incorrectly, other per game stats can be provided such as rebounds, assists, age, and team he currently plays for. After each clue, the user will be able to input another NBA player. I will give them five guesses, and at that point, provide them with the correct answer and a prompt to play again.

## Install/deployment/admin issues:
If the user guide has been read, the project installed, then it is simply running the app to get started. By opening the GUI, the app will begin by selecting a random nba player and displaying the player's points per game.

## User interaction and flow through your code 
Once the project is installed, ensure that json, csv, beautifulsoup, random, tkinter, itertools, and pydoc packages are also installed. After that, the GUI can be launched and the game can begin. As discussed in earlier sections of the developer guide, a random nba player will be selected and the user will see the ppg for that random nba player. The user will be prompted to guess, and then, using loops, four additional hints will be provided. After each hint, the user will be given another chance to guess the NBA player. After five guesses, the game will end and the user will be asked if they would like to play again.

## Known Issues:
No known issues at this time

## Future work:
* Adding a timer, giving the user 10 seconds to make their guess before the next hint is provided
* Additional GUI updates
  * Establish text hierarchy, such as header styles h1-h3 and paragraph text
  * Using colors such as green and red to denote correct or incorrect answers

## Ongoing deployment/development
This game pulls data from a table on nba.com during the 2022-2023 NBA season. As this game continues to be live, it would be beneficial to the user that we update the group of players we are pulling from. The list of players can change from year to year, so for the game to stay "up-to-date", an update at the end of each year is crucial.
