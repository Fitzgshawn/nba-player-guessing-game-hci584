from itertools import count
from pydoc import text
import random
# import random functionality
import csv
# import csv of nba players and statistics from nba.com
def play_again(): # define logic to play again after the end of a game
    print("Do you want to play again?")
    comment = input("Yes or No ")
    if comment == "Yes":
        play_game()
    else: 
        print("thanks for playing!")

def get_random_row(csv_file): # define random selection of an nba player and where it can be found within repository
    with open("data/" + csv_file, "r") as f:   
        reader = csv.reader(f)
        rows = list(reader)

    return random.choice(rows) # return random nba player


def play_game():
    csv_file = "nba_player_list.csv"

    row = get_random_row(csv_file)

    # Define the hints
    random_player = (row[1])
    ppg = (row[30])
    rpg = (row[22])
    apg = (row[23])
    age = (row[5])
    team = (row[4])
 
    # dict for each hint as strings
    hint_dict = {"ppg":[ppg, "points per game"],"rpg": [rpg, "rebounds per game"], "apg":[apg, "assists per game"], "age": [age, "years old"], "team": [team, ""]}

    count = 0 # begin count

    for hint in hint_dict:
        value, text = list(hint_dict.values())[count]
        if count == 0: 
            print(f"This player averages {value} {text}")

        # Get the user's guess
        guess = input("Guess the NBA player's name: ")
        
        count += 1
        if guess == random_player:
            print("Correct! The player's name is", random_player)
            play_again()
        elif count <3: # if count is less than three, loop back to another hint. either ppg, rpg, or apg
            value, text = list(hint_dict.values())[count]
            print(f"Incorrect! Your next hint is: This player averages {value} {text}")
        elif count <4:
            value, text = list(hint_dict.values())[count]
            print(f"Incorrect! Your next hint is: This player is {value} {text}")
        elif count <5:
            value, text = list(hint_dict.values())[count]
            print(f"Incorrect! Your next hint is: This person plays for {value}")

    # Final guess
    if guess == random_player:
        print("Correct! The player's name is", random_player)
        play_again()
    else:
        print(f"Game over! The answer is {random_player}.")
        play_again()

play_game()
