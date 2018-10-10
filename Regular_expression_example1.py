#Program to understand how regular expressions work in Python
# To use regular expressions, we need to import that module as like below
import re

pattern = r"spam"

if re.match(pattern,"spamspamspam"):
	print("Matching")
else:
	print("Not matching")