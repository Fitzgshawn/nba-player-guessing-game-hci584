import csv
import random

def get_random_cell(file_name):
  """
  Returns a random cell from the first column of a .csv file.

  Args:
    file_name: The name of the .csv file.

  Returns:
    A random cell from the first column of the .csv file.
  """

  with open(file_name, "r") as f:
    reader = csv.reader(f)
    cells = [row[0] for row in reader]

  return random.choice(cells)


cell = get_random_cell("data.csv")


# Get the user's guess
guess = input("Guess the NBA player's name: ")

# Check if the user guessed correctly
if guess == random_player:
    print("Correct! The player's name is", random_player)
else:
    # need to figure out how to give hints


# Play again?
play_again = input("Would you like to play again? (y/n): ")

if play_again == "y":
    main()
else:
    print("Thanks for playing!")
