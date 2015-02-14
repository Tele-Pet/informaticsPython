# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40.

hours = float(raw_input('Enter hours: '))
rate = float(raw_input('Enter rate: '))
if hours > 40:
	overtime = hours % 40
	pay = ((overtime * 1.5)  * rate) + (40 * rate)
	print "Cha-Ching!  That's overtime.  Total pay is: ", pay
else:
	pay = hours * rate
	print "Thanks for your work.  Total pay is: ", pay