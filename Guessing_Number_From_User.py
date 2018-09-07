#Program to guess a number by the user from provided random number from 1 to 9 till user says "exit"

#importing random, this alows us to generate the random numbers in between the given range
import random

#Let's ask to pick a random number between 1 and 9
ran = random.randint(1,9)

#Let't initiate some variables for guess and count as 0
guess = 0
count = 0

#We will use while loop here to check that "guess is not the random number" and "guess is not exit"
while guess != ran and guess != 'exit':
	guess = int(input("Provide a number to see if you are guessed it correctly or not : "))

	#if loop to see if the guess = exit or not
	if guess == 'exit':
		break

	guess = int(guess)
	count += 1

	if guess < ran:
		print("The number {0} you provided is less than randon number".format(guess))
	elif guess > ran:
		print("The number {0} you provided is higher than random number".format(guess))
	else:
		print("Superb, you expected it right. The number {0} you provided is exactly same as the random number: {0})".format(guess,ran))
		print('And you have taken',count,'tries to guess it')