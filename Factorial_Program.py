#Program to find the factorial of a given number

def fact(number):
	if number == 0:
		return 1
	else:
		return number * (number-1)

#Ask the user to provide a number
number = int(input("Please provide a number to find the factorial: "))
print ("The factorial of a provided number is",fact(number))