# import nba player data
players = ['nba_data.csv'
]

# Choose a random player
random_player = random.choice(players)

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
