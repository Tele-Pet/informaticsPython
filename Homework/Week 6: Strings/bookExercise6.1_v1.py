# Exercise 6.1 Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

myString = 'Josiah'
myStringLength = len(myString)
myBackwardString = -1 * myStringLength
index = -1

while index >= myBackwardString:
	letter = myString[index]
	print letter
	index = index -1



