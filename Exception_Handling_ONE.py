""" This program is to understand how exceptions can be handled in Python 
We can use "try/except" statement for exception handling. 
"""

try:
	#let's ask user to provide the input
	#number1 = input("Provide a number: ")
	#number2 = input("Provide a number to divide: ")

	#Comment the above 2 lines, and uncomment the below 2 lines and execute again
	number1 = int(input("Provide a number: "))
	number2 = int(input("Provide a number to divide: "))
	print(number1/number2)
	print("Calcuation is done")
# It will execute when the user provides the number2 as 0
except ZeroDivisionError:
	print("An error occured due to zero division")

# It will execute when the user runs the code with first 2 lines of code
except TypeError:
	print("An error occured because the user provided strings and trying to do a mathematical operation on strings")

# It will execute when the user provides the number1 or number2 as a string or letter "a"
except ValueError:
	print("User has provided a string in place of integer and hence the ValueError: invalid literal for int() with base 10: 'a'")

