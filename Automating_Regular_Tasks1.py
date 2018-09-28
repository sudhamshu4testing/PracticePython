#This program is to automated the day to day activities using Python3
#This program opens all the websites which I use at 1100 hours IST everyday

import webbrowser

with open("webbrowsers_list.txt") as f:
	for line in f:
		line = line.split()
		webbrowser.open(line[0])
	
