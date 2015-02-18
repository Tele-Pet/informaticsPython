#!/usr/bin/env python
# -*- coding: utf-8 -*-
# WEEK 5: Iteration (5.0 ~ 5.10)
# Before you can update a variable, you have to initialize it, usually with a simple assignment:
# >>>x=0 >>>x=x+1
###############################################################################

# n=5 
# while n > 0:
# 	print n
# 	n = n-1
# print 'Blastoff!'

###############################################################################

# while True:
# 	line = raw_input('> ') 
# 	if line == 'done':
# 		break 
# 	print line
# print 'Done!'

# This way of writing while loops is common because you can check the condition anywhere in the loop (not just at the top) and you can express the stop condition affirmatively (“stop when this happens”) rather than negatively (“keep going until that happens.”).

###############################################################################


# # 'for' loops:
# friends = ['Joseph', 'Glenn', 'Sally'] 
# for friend in friends:
# 	print 'Happy New Year:', friend 
# print 'Done!'

###############################################################################

# We set the variable count to zero before the loop starts, then we write a for loop to run through the list of numbers. Our iteration variable is named itervar and while we do not use ITERVAR in the loop, it does control the loop and cause the loop body to be executed once for each of the values in the list.

# count = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
# 	count = count + 1 
# 	print 'Count: ', count

###############################################################################

# total = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
# 	total = total + itervar 
# 	print 'Total: ', total

###############################################################################

# None is a special constant value which we can store in a variable to mark the variable as “empty”.

# largest = None
# print 'Before:', largest
# for itervar in [3, 41, 12, 9, 74, 15]:
# 	if largest is None or itervar > largest: 
# 		largest = itervar
# 	print 'Loop:', itervar, largest 
# 	print 'Largest:', largest

###############################################################################

# smallest = None
# print 'Before:', smallest
# for itervar in [3, 41, 12, 9, 74, 15]:
# 	if smallest is None or itervar < smallest: 
# 		smallest = itervar
# 	print 'Loop:', itervar, smallest 
# 	print 'Smallest:', smallest

###############################################################################

# def min(values): 
# 	smallest = None
# 	for value in values:
# 		if smallest is None or value < smallest:
# 			smallest = value 
# 	return smallest

# values = [1, 10, 500, -5]
# print min(values) # Output: -5

###############################################################################

# def max(values):
# 	'''Enter a list of number values'''
# 	largest = None
# 	for value in values:
# 		if largest is None or value > largest:
# 			largest = value
# 	return largest

# values = [ 1, 10, 500, -5]
# print max(values) # Output: 500

###############################################################################

# min & max are built-in functions too

# print min([1, 10, 500, -5]) #Etc...

###############################################################################

# import numpy as np
# values = [ 1, 10, 500, -5]
# oldSkoolMean = float(sum(values)) / len(values)

# print 'Mean via np: ', np.mean(values)
# print 'Mean via oldSkoolMean: ', oldSkoolMean

###############################################################################




