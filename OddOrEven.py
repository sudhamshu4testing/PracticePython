#Program to find even or odd number

#Ask user to input a number
number = int(input("Enter a number: "))

#Program to find the provided number is even or odd
#Let us use if condition to derive this

if (number%2) == 0:
	print("The provided number {0} is an even number".format(number))
else:
	print("The provided number {0} is an odd number".format(number))