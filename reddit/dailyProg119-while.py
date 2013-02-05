def givechange():

	number = input("How much money?:")
	quarters = 0
	dimes = 0
	nickles = 0
	pennies = 0
	quarter_count = 0
	dime_count = 0
	nickle_count = 0
	penny_count = 0

	while number >= .25:
		number -= .25
		quarter_count += 1
	else:
		while number >= .10:
			number -= .10
			dime_count += 1
		else:
			while number >= .05:
				number -= .05
				nickle_count += 1
			else:
				while number > .00:
					number -= .01
					penny_count += 1
				else:
					pass
					
	if quarter_count > 0:
		print "quarters: %r" % quarter_count
	if dime_count > 0:
		print "dimes: %r" % dime_count
	if nickle_count > 0:
		print "nickles: %r" % nickle_count
	if penny_count > 0:
		print "pennies: %r" % penny_count

givechange()
