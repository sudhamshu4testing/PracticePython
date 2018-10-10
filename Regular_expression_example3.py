"""Program to understand how regular expressions work in Python
To use regular expressions, we need to import that module as like below"""
import re

pattern = r"pam"

""" re.search() returns an object with several methods that give details about it.
The following are these methods
group() - which returns the string matched
start() and end() - which return the start and ending positions of the first match
span() - which returns the start and end positions of the first match as tuple"""

match  = re.search(pattern,"eggspamsausage")
if match:
	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())