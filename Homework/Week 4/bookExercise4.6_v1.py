# Exercise 4.6 Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45 Enter Rate: 10 Pay: 475.0


def computepay(hours, rate):
	if hours > 40:
		overtime = hours % 40
		pay = ((overtime * 1.5)  * rate) + (40 * rate)
		print "Cha-Ching!  That's overtime.  Total pay is: ", pay
	else:
		pay = hours * rate
		print "Thanks for your work.  Total pay is: ", pay

hours = float(raw_input('Enter hours: '))
rate = float(raw_input('Enter rate: '))
computepay(hours, rate)

# if hours > 40:
# 	overtime = hours % 40
# 	pay = ((overtime * 1.5)  * rate) + (40 * rate)
# 	print "Cha-Ching!  That's overtime.  Total pay is: ", pay
# else:
# 	pay = hours * rate
# 	print "Thanks for your work.  Total pay is: ", pay