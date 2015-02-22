# Watching this video called Loop Like A Native:
# https://www.youtube.com/watch?v=EnSu9hHGq5o#t=148

theAddress = ("/Users/josiah_MBP/Dropbox/Documents/School/Coursera/PythonGIT/Homework/explorePython/gettysburgAddress.txt")

with open(theAddress) as f:
	for line in f: # see below notes on what repr() is
		print repr(line)




'''
repr(object)
Return a string containing a printable representation of an object. This is the same value yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operation as an ordinary function. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a __repr__() method.
'''

###############################################################################