#Program to sort the words in alphabetical order

# input(): returns integer if integer is entered, and string if string is entered 
#str = input("Enter the text: ")

#raw_input(): returns only string for whatever the value is entered
str = raw_input("Enter the text: ")

#breaking down the string in to a list of words
words = str.split()

#sorting the list of words
words.sort()


print ("The sorted words are:") 
for word in words:     
	print(word)
