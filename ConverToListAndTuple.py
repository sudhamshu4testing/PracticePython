#Program to convert the user entered values to List and Tuple

#Ask user to provide a sequence of comma seperated numbers
numbers = input("Proved the sequence of comma seperated numbers: ")

l = list(numbers)
#list can also be written as follow
#l = numbers.split(",")
t = tuple(numbers)

print("The sequence of the numbers you provided are converted to list as: ",l)
print("The sequence of the numbers you provided are converted to tuple as: ",t)