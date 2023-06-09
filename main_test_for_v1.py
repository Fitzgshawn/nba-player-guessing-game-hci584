import random

# import nba player data
players = [
]

# Choose a random player
random_player = random.choice(players)

# Get the user's guess
guess = input("Guess the NBA player's name: ")

# Check if the user guessed correctly
if guess == random_player:
    print("Correct! The player's name is", random_player)
else:
    print("Incorrect! The player's name is", random_player)
    hint_number = 1
    while guess != random_player and hint_number <= 3:
        if guess > random_player:
            print("The player's name is less than", guess)
        else:
            print("The player's name is greater than", guess)
        guess = input("Guess the NBA player's name: ")
        hint_number += 1
    if guess == random_player:
        print("Correct! The player's name is", random_player)
    else:
        print("You are out of hints! The player's name is", random_player)

# Play again?
play_again = input("Would you like to play again? (y/n): ")

if play_again == "y":
    main()
else:
    print("Thanks for playing!")
