# import the random package so that we can generate a 
from random import randint
import time
from gamefunctions import winlose, gameVars



print ("\n\n\n\n\n\033[35m Welcome to the game of Rock Paper Scissors\033[30;0;0m")


while player is False:

	#set payer to True	
	print("******************************\n")
	print("gameVars.Computer lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print ("****************************\n\n")
	print ("Chose your wepon!\n\n")
	print ("****************************\n\n")


	player = input("choose rock or paper or scissors\n\n")


	print ("gameVars.computer chose ", gameVars.gameVars.computer, "\n")
	print ("player chose ", player, "\n")

	if ( player == "quit" ):
		exit()
		print ("\n\n\n")
		#Checks if the player wants to quit before any game happens
		#Prints a few lines for replay clarity

	print( "\n \033[31m      gameVars.computer chose:    ", gameVars.gameVars.computer)
	print("\033[32m       player chose:      ", player,"\n \033[30;0;0m")
	#displays what each player chose, if the player did not choose quit
	
	#proceeds to check who the winner is, and prints the result
	

	compare.comparing(player, gameVars.computer)

	# if ( player == gameVars.computer ):
	# 	print("*******Tie!*******")

	# elif ( player == "rock" ):
	# 	if (gameVars.computer == "paper"):
	# 		print("*******You Lose!*******", gameVars.computer, "covers", player, "\n")
	# 		player_lives = player_lives - 1
	# 		gameVars.computer_lives = gameVars.computer_lives + 1
	# 		print("************¯\_(ツ)_/¯************\n")

	# 	elif (gameVars.computer == "scissors"):
	# 		print("*******You WIN!*******", player, "smashes", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives - 1
	# 		player_lives = player_lives + 1
	# 		print("************ʕ￫ᴥ￩ʔ************\n")

	# elif ( player == "paper"):
	# 	if (gameVars.computer == "scissors"):
	# 		print("*******You Lose!*******", gameVars.computer, "cuts", player, "\n")
	# 		player_lives = player_lives - 1
	# 		gameVars.computer_lives = gameVars.computer_lives + 1
	# 		print("************(＾◡＾)っ✂❤ ************\n")
	# 	elif (gameVars.computer == "paper"):
	# 		print("*******You WIN!*******", player, "covers", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives - 1
	# 		player_lives = player_lives + 1
	# 		print("************(ㆁᴗㆁ✿)************\n")

	# elif ( player == "scissors" ):
	# 	if (gameVars.computer == "rock"):
	# 		print("*******You Lose!*******", gameVars.computer, "smashes", player, "\n")
	# 		player_lives = player_lives - 1
	# 		gameVars.computer_lives = gameVars.computer_lives + 1
	# 		print("************¯\_(ツ)_/¯************\n")
	# 	elif (player == "rock"):
	# 		print("*******You WIN!*******", player, "smashes", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives - 1
	# 		player_lives = player_lives + 1
	# 		print("************ʕ·ᴥ-　ʔ************\n")

	# else:
	# 	print("******************************\n")
	# 	print("That's not a valid choice, try again")
	# 	print("******************************\n")

	if player_lives == 0:
		winlose.winolose(" lose!")

	if gameVars.computer_lives == 0:
		winlose.winolose(" win!")


	# if player_lives is 0:
	# 	winorlose("won")
	# 	print("Out of Lives! Would you like to give ita try again?\n")
	# 	choice = input("Y / N")
	# 	print(choice)

	# 	if (choice is "N") or (choice is "n"):
	# 		print("You chose to quit.")
	# 		exit()

	# 	elif (choice is "Y") or (choice is "y"):
	# 		player_lives = 5
	# 		gameVars.computer_lives =5
	# 		player = False
	# 		gameVars.computer = choice[randint(0, 2)]

	# elif gameVars.computer_lives is 0:
	# 	print("You WIN!! Would you like to give it a try again?\n")
	# 	choice = input("Y / N")
	# 	print(choice)

	# 	if (choice is "N") or (choice is "n"):
	# 		print("You chose to quit.")
	# 		print("*********✧ ✰ ｡(♡´❍`♡)*✧ ✰ ｡*********\n")
	# 		exit()

	# 	elif (choice is "Y") or (choice is "y"):
	# 		player_lives = 5
	# 		gameVars.computer_lives =5

	# 	else: player = False
	# 		gameVars.computer = choice[randint(0, 2)]

	# need to check all of our conditions after checking for a tie
	player = False
	gameVars.computer = gameVars.choices[randint(0, 2)]
