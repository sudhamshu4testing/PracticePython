#Program to understand the regular expressions in detail

import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact test@email.com"

match = re.search(pattern,str)
if match:
	print(match.group())