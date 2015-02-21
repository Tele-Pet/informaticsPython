usrInput = 0
usrMax = 0
usrMin = 0

while True:
	usrInput = raw_input("Please enter a number: ")
	if usrInput == "done":
		break
	try:
		usrInput = float(usrInput)
		if usrMin == 0:
			usrMin = usrInput
		if usrInput > usrMax:
			usrMax = usrInput
		if usrInput < usrMin:
			usrMin = usrInput
	except:
		print "That ain't no number..."

print "Largest number entered:", usrMax
print "Smallest number entered:", usrMin