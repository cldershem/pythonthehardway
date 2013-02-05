def givechange():

	number = input("How much money?:")
	quarters = 0
	dimes = 0
	nickles = 0
	pennies = 0

	if number >= .25:
		quarters = int(number/.25)
		qtotal = float(quarters * .25)
		afterq = number - qtotal
	else:
		qtotal = 0
		afterq = number

	if afterq >= .10:
		dimes = int(afterq/.10)
		dtotal = float(dimes * .10)
		afterd = afterq - dtotal
	else:
		dtotal = 0
		afterd = afterq

	if afterd >= .05:
		nickles = int(afterd/.05)
		ntotal = float(nickles * .05)
		aftern = afterd - ntotal
	else:
		ntotal = 0
		aftern = afterd

	if aftern >= .01:
		pennies = int(aftern/.05)
		ptotal = aftern
		afterp = aftern - ptotal
		if afterp != 0:
			print "WHOA!  Hold your roll.  You broke the maths."
			print "%r remaining.  How did you break it?" % afterp
			exit(1)
	else:
		ptotal = 0

	total = qtotal + dtotal + ntotal + ptotal

	if quarters != 0:
		print "quarters:\t\t%r\t%r" % (quarters, qtotal)
		print "dimes:\t\t\t%r\t%r" % (dimes, dtotal)
		print "nickles:\t\t%r\t%r" % (nickles, ntotal)
		print "pennies:\t\t%f\t%f" % (pennies, ptotal)
		print "total:\t\t\t\t%f" % total

givechange()
