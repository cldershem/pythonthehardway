def counting_while(x):
	i = 1
	numbers = []
	while i <= 500:
		print "At the top i is %d" % i
		numbers.append(i)

		i += i
	 	print "Numbers now: ", numbers
	    	print "At the bottom i is %d" % i
	return numbers

x = int(raw_input("Number?: "))

numbers = counting_while(x)
print "The numbers: "
for num in numbers:
	print num

#extra credit
def counting_for(x):
	i = 1
	numbers = []
	for i in range(x,8):
		print "At the top i is %d" % i
		numbers.append(i)

	 	print "Numbers now: ", numbers
	    	print "At the bottom i is %d" % i
	return numbers

x = int(raw_input("Number?: "))
numbers = counting_for(x)
print "The numbers: "
for num in numbers:
	print num
