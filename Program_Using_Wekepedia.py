# Program to get the data from Wikepdia using "wekepedia" module
# Make sure you install "wikipedia" before running this program
# pip3 install wikepedia

import wikipedia

tag = input("Provide the keyword to search the wikipedia page: ")

result = wikipedia.page(tag)
print(result.summary)