import random
import csv
def play_again():
    print("Do you want to play again?")
    comment = input("Yes or No ")
    if comment == "Yes":
        play_game()
    else: 
        print("thanks for playing!")

# CH I changed the path to the csv file ...
def get_random_row(csv_file):
    with open("data/" + csv_file, "r") as f:   
        reader = csv.reader(f)
        rows = list(reader)

    return random.choice(rows)
def play_game():
    csv_file = "nba_player_list.csv"

    row = get_random_row(csv_file)

    # Define the hints  CH: you should line up your comments withing the block structure
    random_player = (row[1])
    ppg = (row[30])
    rpg = (row[22])
    apg = (row[23])
    age = (row[5])
    team = (row[4])
    # Give the user the points per game 
    print(f"This player averages {ppg} points per game")

    # CH why not use a loop for this?
 
    # Make a dict with anything that varies for each hint, here its just one string but 
    # if you need more just make it a list of strings
    # Or you could have a dict as dict value instead of a list ...
    hint_dict = {"rpg": [rpg, "rebounds per game"], "apg":[apg, "assists per game"]}

    for hint in ["rpg", "apg"]: # could be random ...

        # Get the user's guess
        guess = input("Guess the NBA player's name: ")

        if guess == random_player:
            print("Correct! The player's name is", random_player)
            play_again()
        else:
            value, text = hint_dict[hint]  # unroll the 2 list elements into 2 variables
            print(f"Incorrect! Your next hint is: This player averages {value} {text}")

'''
    # Check if the user guessed correctly
    if guess == random_player:
        print("Correct! The player's name is", random_player)
        play_again()
    else:
        print(f"Incorrect! Your next hint is: This player averages {rpg} rebounds per game")

    # Get the user's guess
    guess = input("Guess the NBA player's name: ")

    # Check if the user guessed correctly
    if guess == random_player:
        print("Correct! The player's name is", random_player)
        play_again()
    else:
        print(f"Incorrect! Your next hint is: This player averages {apg} assists per game")

    # Get the user's guess
    guess = input("Guess the NBA player's name: ")

# Check if the user guessed correctly
    if guess == random_player:
        print("Correct! The player's name is", random_player)
        play_again()
    else:
        print(f"Incorrect! Your next hint is: This player is {age} years old")

# Get the user's guess
    guess = input("Guess the NBA player's name: ")

# Check if the user guessed correctly
    if guess == random_player:
        print("Correct! The player's name is", random_player)
        play_again()
    else:
        print(f"Incorrect! Your final hint is: This player plays for {team}")

# Get the user's guess
    guess = input("Guess the NBA player's name: ")

# Final guess
    if guess == random_player:
        print("Correct! The player's name is", random_player)
        play_again()
    else:
        print(f"Game over! The answer is {random_player}.")
        play_again()

'''
play_game()
