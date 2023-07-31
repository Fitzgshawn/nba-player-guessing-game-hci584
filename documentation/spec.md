Title: Guess the NBA player 


### Describe the project in a few paragraphs 

 This app will generate a random player from a list of current NBA players. The user will be able to make an initial guess at who the player is by typing into an input field and submitting, If the user is incorrect, I will provide them with the team that the number of minutes per game the player played last season.  

As the user continues to guess incorrectly, other per game stats can be provided such as points, rebounds, assists, and field goal percentage, and team he currently plays for. After each clue, the user will be able to input another NBA player. I will give them five guesses, and at that point, provide them with the correct answer and a prompt to play again.  

I’ll use basic UI elements to design a clean layout that clearly provides designated spaces for input fields vs the hints being provided. One input field will be shown at a time, with others showing as needed, to avoid any confusion for the user. I’d also like to include directions like the first paragraph on this spec document to give users an understanding of how to play the game before starting. 

### Who would be the users? Are there secondary stakeholders? 

My primary user would be basketball fans that are hoping to test their NBA knowledge against their friends and colleagues. Assuming I could pull in over 300 players from all the NBA teams, it would mean that users would need to be familiar with today’s NBA players and their individual statistics.  

### What problem would it (help to) solve? 

 I think this app could help build knowledge of NBA fans everywhere. Users could better understand the statistics of each NBA player this year, and the guessing aspect could add an element of fun and competitiveness to all. 

- What is the workflow (user path)? What would the user do? What is the primary interaction? Is there an interaction loop? 

User lands on the page and is given an initial hint: The field goal percentage for a particular basketball player. User is prompted to enter a basketball player's name in the text field and submit. If they are correct, they are given a success message and the game is over. If not, an additional hint is provided. Points per game is the next hint, then they are prompted to guess again. The pattern continues with rebounds per game, assists per game, and finally the team they play for. After those five hints, the user is given the answer and the game is over.  

- What data would be used (input), how would you get it and how is it processed/analyzed? 

Data will come from scrape of https://basketball.realgm.com/nba/stats    

I can request player names from the column on that site, which will then be compared against the guesses input by the user. Additionally, the data used for hints can also be retreived from that same site.  

- What are the results and how are they presented?  

 Results for the user will be “Congratulations! You guessed the correct answer” if at any point their guess matches the NBA player that has been randomly selected. Otherwise, the user will see “The shot is up and...you missed. Guess again”. After five guesses, the message will read “And that’s the end of the game. You’ll get them next time!” 

 

Mockup 

 

 

Flow chart 

 
