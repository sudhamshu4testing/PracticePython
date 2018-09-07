#Program to count the number of upper and lower letters in a giving string using functions

def string(s):
	d = {"UC":0, "LC":0}
	for c in s:
		if c.isupper():
			d["UC"] += 1
		elif c.islower():
			d["LC"] += 1
		else:
			pass
	print ("Original String is: ",s)
	print ("Number of upper case letters are: ", d["UC"])
	print ("Number of lower case letters are: ", d["LC"])

a = input("Please provide a string to count the upper and lower case letters: ")
string(a)