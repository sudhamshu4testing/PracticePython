#Program to overlap a list

def intersection(a,b):
	#1 method
	#return list(set(a) & set(b))

	#Other method
	#return set(a).intersection(b)

	#One more method
	temp = set(b)
	ls = [value for value in a if value in temp]
	return ls

a = [1,2,3,4,5]
b = [1,2,3,4,6]

print(intersection(a,b))