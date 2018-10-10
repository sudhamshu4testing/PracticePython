#Program to understand how a class works

class Dog:
	def __init__(self,name,color):
		self.name = name
		self.color = color

	def bark(self):
		print("Woof!")

fido = Dog("Fido","Brown")
print(fido.name)
fido.bark()