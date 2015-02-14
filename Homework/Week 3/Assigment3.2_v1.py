# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.

# THIS IS A TEST	

'''
Example:
- - - - 
Enter hours: 20
Enter rate: 	nine
Error, please enter numeric input
'''

hours = 0
while True:
	try:
		hours = float(raw_input('Enter hours: '))
	except:
		print 'Error, please enter numeric input'

rate = 0
while True:
	try:
		rate = float(raw_input('Enter rate: '))
	except:
		print 'Error, please enter numeric input'

if hours > 40:
	overtime = hours % 40
	pay = ((overtime * 1.5)  * rate) + (40 * rate)
	print "Cha-Ching!  That's overtime.  Total pay is: ", pay
else:
	pay = hours * rate
	print "Thanks for your work.  Total pay is: ", pay



'''
>>> while True:
...     try:
...         x = int(raw_input("Please enter a number: "))
...         break
...     except ValueError:
...         print "Oops!  That was no valid number.  Try again..."
...
'''