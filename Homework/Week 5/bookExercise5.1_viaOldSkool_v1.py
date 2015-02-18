#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Exercise 5.1 Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.33333333333

usrInput = 0
usrSum = 0
usrCount = 0
usrAvg = 0
while usrInput != 'done':
	usrInput = raw_input('Enter a number: ')
	try:
		usrInput = float(usrInput)
		usrSum += usrInput
		usrCount += 1
		usrAvg = usrSum / usrCount
		# print 'usrCount is: ', usrCount
		# print 'usrSum is: ', usrSum
		# print 'usrAvg is: ', usrAvg
	except:
		if usrInput == 'done':
			print 'User avereage is: ', usrAvg
		else:
			print 'Invalid input'

