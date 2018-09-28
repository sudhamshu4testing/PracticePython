# Program to find the location and address using geopy module
# Before running this program make sure you installed "geopy" module
# pip3 install geopy

import wikipedia

tag = input("Provide the keyword to search the wikipedia page: ")

result = wikipedia.page(tag)
print(result.summary)