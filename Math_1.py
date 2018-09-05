#Program to ask the user to provide name and age, and calculate when the user turns 100

#Ask user to provide name and age
name = raw_input("Enter your name: ")
age = int(input("Enter your age: "))

years = (100 - age)

print("Hi {0} you will turn 100 in {1} years from now".format(name,years))