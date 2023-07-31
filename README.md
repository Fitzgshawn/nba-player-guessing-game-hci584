# nba-player-guessing-game-hci584
A guessing game that randomly selects an NBA player from the 2022-23 season, then provides five hints to the user in order for them to correctly guess the player.

## **Description**
This app will generate a random player from a list of current NBA players. The list of NBA players comes from NBA.com, more specifically their stats page. The website gathers statistics from every active player from the 2022-2023 NBA season. All of the table data is scraped directly from the NBA.com site, and placed into a table, saved as a .csv file. The GUI requests a random NBA player for the game to begin, and highlights the columns of the table that need to be pulled in for the game to begin, such as player's name, points per game, rebounds per game, assists per game, age, and the players team during the 2022-2023 NBA season.

The app will provide the points per game for the random player and the user will be prompted to make their first guess. The user will make an initial guess by typing into an input field and submitting, If the user is incorrect, the app will provide them with a hint. As the user continues to guess incorrectly, other per game stats can be provided such as rebounds, assists, age, and team he currently plays for. After each clue, the user will be able to input another NBA player. I will give them five guesses, and at that point, provide them with the correct answer and a prompt to play again.

## Instructions **
To begin, the user will open the file 'gui.py' in Visual Studio Code, or any other code editor. Once the file is open, select to 'run' the file. A new window will open and the game is ready to begin. An NBA player will have been randomly selected from a list of all active players during the 2022-2023 season, and the points per game of that player will be provided for the user to begin guessing. The user will submit their guess in the text input field, as seen below.
<img width="300" alt="Screen Shot 2023-07-30 at 9 19 25 PM" src="https://github.com/Fitzgshawn/nba-player-guessing-game-hci584/assets/134566446/f487d70c-2e4f-45a3-868e-55cf96c66128">

If the guess is correct, the game is over and the user is prompted to play again. If not, the game will continue and another hint is provided. 
<img width="300" alt="Screen Shot 2023-07-30 at 9 20 55 PM" src="https://github.com/Fitzgshawn/nba-player-guessing-game-hci584/assets/134566446/0d381ec1-43dc-49e6-ad47-e82e8c051b83">

If the user continues to guess incorrectly, this pattern will continue. The additional hints will display to provide clarity for the user, including assists per game, player's age, and the team a person plays for. If the user is still unable to answer correctly after the hints, the name of the correct NBA player will be provided to the user and the game will be over. The user is then asked if they would like to play again.

## **Authors**
Shawn Fitzgerald

## **Version History**
0.1
Initial Release

## **License**
This project is licensed - see the LICENSE.md file for details

## **Acknowledgments**
Appreciate Prof. Harding for all of the guidance
[@ChHarding](https://github.com/ChHarding)
