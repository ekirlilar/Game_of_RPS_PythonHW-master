from random import randint
choices = ["rock", "paper", "scissors"]
computer = choices[randint(0, 2)]
player = False


def weapon(status):
	print("Choose your weapon!\n")
	print("******💎*☐*✄******\n")

	if (player == "rock"):
		print("You choose 💎 ", player, "\n")

	if (player == "paper"):
		print("You choose ☐ ", player, "\n")

	if (player == "scissors"):
		print("You choose ✄ ", player, "\n")







	if ( player == computer ):
		print("*******Tie!*******")

	elif ( player == "rock" ):
		if (computer == "paper"):
			print("*******You Lose!*******", computer, "covers", player, "\n")
			player_lives = player_lives - 1
			computer_lives = computer_lives + 1
			print("************¯\_(ツ)_/¯************\n")

		elif (computer == "scissors"):
			print("*******You WIN!*******", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1
			player_lives = player_lives + 1
			print("************ʕ￫ᴥ￩ʔ************\n")

	elif ( player == "paper"):
		if (computer == "scissors"):
			print("*******You Lose!*******", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
			computer_lives = computer_lives + 1
			print("************(＾◡＾)っ✂❤ ************\n")
		elif (computer == "paper"):
			print("*******You WIN!*******", player, "covers", computer, "\n")
			computer_lives = computer_lives - 1
			player_lives = player_lives + 1
			print("************(ㆁᴗㆁ✿)************\n")

	elif ( player == "scissors" ):
		if (computer == "rock"):
			print("*******You Lose!*******", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
			computer_lives = computer_lives + 1
			print("************¯\_(ツ)_/¯************\n")
		elif (player == "rock"):
			print("*******You WIN!*******", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1
			player_lives = player_lives + 1
			print("************ʕ·ᴥ-　ʔ************\n")

	else:
		print("******************************\n")
		print("That's not a valid choice, try again")
		print("******************************\n")