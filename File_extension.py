#Program to accept a file name from the user and print the extension

#Ask the user to provide a file name with extension
file_name = raw_input("Please provide a file name with extension: ")
extention = file_name.split(".")[-1]

print("File extension is :", extention)