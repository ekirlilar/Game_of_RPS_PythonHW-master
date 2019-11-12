import time
from random import randint


def comparing (player, computer):
	global player_lives
	global computer_lives
	global player
	global computer
	global choices

	if ( player == computer ):
		print("*******Tie!*******")

	elif ( player == "rock" ):
		if (computer == "paper"):
			print("*******You Lose!*******", computer, "covers", player, "\n")
			player_lives = player_lives - 1
			gameVars.computer_lives = gameVars.computer_lives + 1
			print("************¯\_(ツ)_/¯************\n")

		elif (gameVars.computer == "scissors"):
			print("*******You WIN!*******", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1
			player_lives = player_lives + 1
			print("************ʕ￫ᴥ￩ʔ************\n")

	elif ( player == "paper"):
		if (gameVars.computer == "scissors"):
			print("*******You Lose!*******", gameVars.computer, "cuts", player, "\n")
			player_lives = player_lives - 1
			gameVars.computer_lives = gameVars.computer_lives + 1
			print("************(＾◡＾)っ✂❤ ************\n")
		elif (gameVars.computer == "paper"):
			print("*******You WIN!*******", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1
			player_lives = player_lives + 1
			print("************(ㆁᴗㆁ✿)************\n")

	elif ( player == "scissors" ):
		if (gameVars.computer == "rock"):
			print("*******You Lose!*******", gameVars.computer, "smashes", player, "\n")
			player_lives = player_lives - 1
			gameVars.computer_lives = gameVars.computer_lives + 1
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