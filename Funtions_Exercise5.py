#Program to calculate tax (provided by the user) on the bill using function
#Defining a function

def tax(bill_amount):
	#Ask user to provde the tax amount 
	percentage = input("What is the tax percentage? ")
	bill_amount *= percentage
	return bill_amount

billed_amount = int(input("Enter the bill amount: "))
final_bill = tax(billed_amount)

print("The total amount you have to pay with the tax is:", final_bill)


