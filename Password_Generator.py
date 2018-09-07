#Program to generate a random password

import random

ch = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	  "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
	  "1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")"]

password_strength = raw_input("What is the password strength you are looking for: 'weak','medium','strong': ").lower()

new_password= []

def password(strengtht):
	if password_strength == 'weak':
		while len(new_password) !=5:
			new_password.append(ch[random.randint(1,70)])
	elif password_strength == 'medium':
		while len(new_password) !=8:
			new_password.append(ch[random.randint(1,70)])
	elif password_strength == 'strong':
		while len(new_password) != 14:
			new_password.append(ch[random.randint(1,70)])
	return new_password

password(password_strength)
new_password = "".join(new_password)

print("The randomly generated password is {0}".format(new_password))

