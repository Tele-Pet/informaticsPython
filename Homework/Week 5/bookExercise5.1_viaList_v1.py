#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Exercise 5.1 Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.33333333333

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
			print 'List average is ', np.mean(usrList)
		else:
			print 'Invalid input'

		