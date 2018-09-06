#Program for a game to play between 2 users and decide who wins the "Rock, Scissor and Paper" game

#Importing "sys" module to use "exit"
import sys

#Let's say if user1 selects "Rock" and user2 selects "Scissor", user1 will win because "Scissor" can't break the rock
#Similar way if user1 selects "Paper" and user2 selects "Scissor", user2 will will because "Scissor" can cut paper

#Let's ask users to provide their names
first_user_name = raw_input("What's your name? ")
second_user_name = raw_input("And what is your's? ")

#Let's ask users to provide their answers to decide who wins
first_user_answer = raw_input("%s, Do you want to choose Rock, Scissor or Paper? " %first_user_name)
second_user_answer= raw_input("%s, Do you want to choose Rock, Scissor or Paper? " %second_user_name)

#Writing a function to compare and decide who wins
def compare(user1,user2):
	# If both the users choosed the same option
	if user1 == user2:
		return("It is a tie!")
	elif user1 == 'Rock':
		if user2 == 'Scissor':
			return("Rock wins!")
		else:
			return("Paper wins!")
	elif user1 == 'Scissor':
		if user2 == 'Paper':
			return("Scissor wins!")
		else:
			return("Rock wins!")
	elif user1 == 'Paper':
		if user2 == 'Rock':
			return("Rock wins!")
		else:
			return("Scissor wins!")
	else:
		return("Invalid input. You have not choose any of the options above mentioned")
		sys.exit()

print(compare(first_user_answer,second_user_answer))
