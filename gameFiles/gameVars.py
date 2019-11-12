#set up some variables for player and AI lives
player_lives = 5
computer_lives = 5

# choices is an array is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0, 2)]

player = input("choose rock, paper or scissors\n\n")

# set up the loop so we don't have to restart all the time
player = False