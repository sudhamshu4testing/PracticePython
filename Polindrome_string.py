#Program to find whether a provided string by user is Polindrome or not

#Ask the user to provide a string

test_string = raw_input("Enter a string: ")

#We should change the provided word to case insenesitive
test_string = test_string.lower()

#Using "rvs" method to reverse the string
rvs = test_string[::-1]
print ("Provided word is {0}".format(test_string))
print ("Reveresed word is {0}".format(rvs))

#If the word and the reversed word are same then it is polindrome
if test_string == rvs:
	print("Provided word is a polindrome")
else:
	print("Provided word is not a polindrome")