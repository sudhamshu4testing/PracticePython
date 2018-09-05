#Program to return the difference between "Max" and "Min" value from a list

def range_with_negatives():
	l = [1,-3,5,2,4,9,3,8,23]
	return (max(l) - min(l))

def range_without_negatives():
	a = [1,2,3,4,5,6,7,8,9]
	return (max(a) - min(a))

print (range_with_negatives())
print (range_without_negatives())
