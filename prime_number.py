#Python program to check if a number is prime or not

#Take input from the user
num = int(input("Enter a number:"))

# 0 and 1 are not prime numbers, hence checking if the given number is greater than 1 or else it prints it as not a prime number
if num > 1:
	#check for factors
	for i in range(2,num):
		# If the reminder is equal to 0, it is a prime number. Hence doing modulus here
		if (num%i) == 0:
			print(num,"is not a prime number")
			# Let's say we have give a number as '700', it is not a prime number because the reminder is 0. 350*2 = 750. To display that information added the below print statement
			print(i,"times",num//i,"is",num)
			break
	else:
		print(num,"is a prime number")
		
else:
	print(num,"is not a prime number")

