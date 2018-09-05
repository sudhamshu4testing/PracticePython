#Program to find the numbers divisible by 7 and not multiple of 5
a= []
for i in range(2000,3201):
	if (i%7==0) and (i%5!=0):
		a.append(str(i))

print (','.join(a))