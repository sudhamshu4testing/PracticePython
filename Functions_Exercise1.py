#Program shows how to work with functions in python

def showModuleName():
	print(__doc__)

def getModuleFile():
	return __file__

a = showModuleName()
b = getModuleFile()

print(a)
print(b)