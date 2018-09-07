#Program to shut down using function

def shut_down(s):
	if s == 'yes':
		#return "Shutting down"
		print ("Shutting down")
	elif s == 'no':
		#return "Shutdown aborted"
		print("Shutdown aborted")
	else:
		#return "Sorry"
		print("Sorry this is not a correct option")

a = input("Enter an option as 'yes' or 'no' to Shutdown: ")
shut_down(a)
