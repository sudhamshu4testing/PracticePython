"""Program to understand how regular expressions work in Python
To use regular expressions, we need to import that module as like below"""
import re

pattern = r"spam"

""" re.match() has other functions to match patterns which are re.search() and re.findall()
Let's see how they works """

if re.match(pattern,"eggspamsausagespam"):
	print("Matching")
else:
	print("Not matching")

if re.search(pattern,"eggspamsausagespam"):
	print("Matching the search")
else:
	print("Not matching the search")

print(re.findall(pattern,"eggspamsausagespam"))