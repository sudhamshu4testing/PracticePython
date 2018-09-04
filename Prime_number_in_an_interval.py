#Ask the user to enter the smaller and larger numbers
min_range = int(input("Enter a number: "))
max_range = int(input("Enter a number: "))

#print the prime numbers between min_range and max_range
print("Prime numbers between",min_range,"and",max_range,"are:")
for i in range(min_range,max_range+1):
	if i > 1:
		for j in range(2,i):
			if (i%j) == 0:
				break
		else:
			print(i)