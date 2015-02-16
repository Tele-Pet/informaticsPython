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

def getHrsRate():
	# hours = 0
	# while hours == 0:
	while True:
		try:
			hours = float(raw_input('Enter hours: '))
			break
		except:
			print 'Not a number.  Try again.'
	while True:
		try:
			rate = float(raw_input('Enter rate: '))
			break
		except:
			print 'Not a number.  Try again.'
	computepay(hours, rate)

getHrsRate()

# if hours > 40:
# 	overtime = hours % 40
# 	pay = ((overtime * 1.5)  * rate) + (40 * rate)
# 	print "Cha-Ching!  That's overtime.  Total pay is: ", pay
# else:
# 	pay = hours * rate
# 	print "Thanks for your work.  Total pay is: ", pay