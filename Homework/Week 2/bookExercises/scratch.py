choice = 'x'
usr_Options()
while choice != "q":
	choice = raw_input("Please enter your choice: ")
	if choice == "1":
		usrPlace_1 = raw_input("\nEnter your first place: ")
		usrPlace_1 = usrPlace_1.title()
		place1_Index = myDictionary[usrPlace_1]
		x1 = float(place1_Index.x_coord)
		y1 = float(place1_Index.y_coord)

		usrPlace_2 = raw_input("\nEnter your second place: ")
		usrPlace_2 = usrPlace_2.title()
		place2_Index = myDictionary[usrPlace_2]
		x2 = float(place2_Index.x_coord)
		y2 = float(place2_Index.y_coord)

		p1 = x1, y1
		p2 = x2, y2

		# usrDist = dist(x2, x1, y2, y1)
		usrDist = distance(p1, p2)

		print "\nThanks.  Computing distance between {0} and {1}...".format(usrPlace_1, usrPlace_2)

		print "\nDistance total"
		print "Meters: ", intWithCommas(int(round(usrDist)))
		print "Kilometers: ", intWithCommas(int(round(usrDist / 1000)))
		print "Miles: ", intWithCommas(int(round(usrDist * 0.00062137)))
		usr_Options()

	elif choice == "2":
		# distanceList = []
		# usrCenterPlace = (raw_input("\nEnter your home center location: "))
		# usrCenterPlace = usrCenterPlace.title()
		# centerPlace_Index = myDictionary[usrCenterPlace]
		# x1 = float(centerPlace_Index.x_coord)
		# y1 = float(centerPlace_Index.y_coord)
		# p1 = x1, y1
		# print p1

		# usrRadius = raw_input("\nEnter the meter radius within which you'd like to search: ")

		# p1 = x1, y1
		# p2 = x2, y2

		# # usrDist = dist(x2, x1, y2, y1)
		# usrDist = distance(p1, p2)

		# for key, value in myDictionary.iteritems():
		# 	allCoords = [x, y]
		# 	allCoords_x2 = allCoords[0]
		# 	allCoords_y2 = allCoords[1]
		print "This functionality is still in progress."
		usr_Options()

		
	elif choice == "q":
                print "",