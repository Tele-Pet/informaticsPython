# Exercise 5.2 Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

# sys.maxint
# The largest positive integer supported by Python’s regular integer type. This is at least 2**31-1. The largest negative integer is -maxint-1 — the asymmetry results from the use of 2’s complement binary arithmetic.

import sys

usrInput = None
usrMin = +sys.maxint
usrMax = -sys.maxint

while usrInput != 'done':
	usrInput = raw_input('Enter a number: ')
	try:
		usrInput = float(usrInput)
		if usrInput < usrMin and usrInput != None:
			usrMin = usrInput
		else:
			if usrInput > usrMax and usrInput != None:
				usrMax = usrInput
	except:
		if usrInput == 'done':
			print 'User max is: ', usrMax
			print 'User min is: ', usrMin
		else:
			print 'Invalid input'
