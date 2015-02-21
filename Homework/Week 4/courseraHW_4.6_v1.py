def computepay(hours, rate):
	if hours > 40:
		overtime = hours % 40
		pay = ((overtime * 1.5)  * rate) + (40 * rate)
		print pay
		return pay
	else:
		pay = hours * rate
		print pay
		return pay

hours = float(raw_input('Enter hours: '))
rate = float(raw_input('Enter rate: '))
computepay(hours, rate)