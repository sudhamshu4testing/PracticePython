#Program to write the content to a file

def main():
	#"w+" creates and writes to a file, if there is no such file
	#"w" only writes to a file which is already existing
	f = open("test.txt", "w+")

	#Looping to enter some data in the file
	for i in range(10):
		f.write("This is the line number %d\r\n" %(i+1))

	#This closes the file when the content is written
	f.close()

if __name__ == "__main__":
	main()

#Open "test.txt" and observe if it has the content which we written in loop