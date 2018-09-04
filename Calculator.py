"""Program to calculate using the arithmetic functions"""

#Function for addition of two numbers
def add(x,y):
	return x+y

#Function for substraction of two numbers
def sub(x,y):
	return x-y

#Function for multiplication of two numbers
def mul(x,y):
	return x*y

#Function for division of two numbers
def div(x,y):
	return x/y

#Function for factor of two numbers
def fac(x,y):
	return x%y


print ("Select Operation.")
print ("1. Addition")
print ("2. Substraction")
print ("3. Multiplication")
print ("4. Division")
print ("5. Factor")

#Ask user to provide the numbers
a = int(input("Give the first number: "))
b = int(input("Give the second number: "))

#Ask user to provide the option
option = input("Select the operand(1/2/3/4/5):")

#We can add this in the print statement, but for the better output I am assigning a variable to each function
c = add(a,b)
d = sub(a,b)
e = mul(a,b)
f = div(a,b)
g = fac(a,b)

#Using if and elif based on the users option
if option == 1 :
	print (a, '+', b, '=', add(a,b))
	print ("Addition of {0} and {1} is {2}".format(a,b,c))

elif option == 2:
	print (a, "-", b, "=", sub(a,b))
	print ("Substraction of {0} and {1} is {2}".format(a,b,d))

elif option == 3:
	print (a, "*", b, "=", mul(a,b))
	print ("Multiplication of {0} and {1} is {2}".format(a,b,e))

elif option == 4:
	print (a, "/", b, "=", div(a,b))
	print ("Division of {0} and {1} is {2}".format(a,b,f))

elif option == 5:
	print (a, "%", b, "=", fac(a,b))
	print ("Factor of {0} and {1} is {2}".format(a,b,g))

else:
	print ("Invalid input")

