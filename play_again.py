import random
import csv
def play_again():
    print("Do you want to play again?")
    comment = input("Yes or No ")
    if comment == "Yes":
        play_game()
    else: 
        print("thanks for playing!")
def get_random_row(csv_file):
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    return random.choice(rows)
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
# Give the user the points per game 
    print(f"This player averages {ppg} points per game")

# Get the user's guess
    guess = input("Guess the NBA player's name: ")

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



