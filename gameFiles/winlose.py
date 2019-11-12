from random import radiant
from gamefiles

def winorlose(status):
	print("called win or lose")
	print("************(ツ)************\n")
	print ("you", status, "!Would you like to play again?")

	choice = input("Y / N")
	print(choice)

	if (choice is "N" ) or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
	
		
		gameVars.player_lives = 5
		gameVars.computer_lives = 5
		gameVars.total_lives= 5
		gameVars.player = False
		gameVars.player = choices[radiant(0,2)]

	else: 
		#use recursion to call winlose again until we get the right input
		#recursion is just
		winorlose(status)