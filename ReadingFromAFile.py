#Program to read the content from a file

f = open("test.txt","r")
message = f.read()
print(message)
f.close()