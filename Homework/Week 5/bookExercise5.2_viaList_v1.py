# Exercise 5.2 Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

import numpy as np

usrInput = None
usrList = []

while usrInput != 'done':	
	usrInput = raw_input('Enter a number: ')
	try:
		usrInput = float(usrInput)
		usrList.append(usrInput)
		print 'Your current list: ', usrList
	except:
		if usrInput == 'done':
			print 'List min is: ', min(usrList)
			print 'List max is: ', max(usrList)
		else:
			print 'Invalid input'