# Exercise 2.5 Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit and print out the converted temperature.

# Testing: 1, 2, 3...

# °C to °F	Multiply by 9, then divide by 5, then add 32
# °F to °C	Deduct 32, then multiply by 5, then divide by 9
# Above retrieved from: http://www.mathsisfun.com/temperature-conversion.html

# Below is a function.  A function is a block of organized, reusable
# code that is used to perform a single, related action. Functions provide
# better modularity for your application and a high degree of code reusing.
def usr_Options():
	print # line to prettify
	print "1) Convert Celsius to Fahrenheit"
	print "2) Convert Fahrenheit to Celsius"
	print "q) Quit"

choice = 'x' # Initialize choice, it needs some value to begin with
usr_Options() # This will run usr_Options, printing all options out
while choice != "q":
	choice = raw_input('Please enter your choice: ')
	if choice == '1':
		usrC = float(raw_input('What is the temperature in celsius? '))
		fahrenheit = (((usrC * 9)/5) + 32)
		print 'The temperature in fahrenheit is approximately {}°F.'.format(fahrenheit)
		usr_Options()
	elif choice == '2':
		usrF = float(raw_input('What is the temperature in Fahrenheit? '))
		celsius = (((usrF - 32) * 5) / 9)
		print 'The temperature in Celsius is approximately {}°C.'.format(celsius)
		usr_Options()
	elif choice == 'q':
		print ''

# Erase this when you see it



