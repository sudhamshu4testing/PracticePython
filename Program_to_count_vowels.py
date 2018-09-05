#Program to count the vowels in a given sentence/word

#Vowels
v = 'aeiou'

statement = 'Sudhamshu'

#Take input from the user
#statement = input("Enter a sentence or word: ")

statement = statement.casefold()

count = {}.fromkeys(vowels,0)

for char in statement:
	if char in count:
		count[char] += 1

print(count)