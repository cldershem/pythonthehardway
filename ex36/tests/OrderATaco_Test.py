from sys import exit

Tortilla_Choices = {'1': 'corn', '2': 'flour'}

taco_order = []
chip_order = []
drink_order = []
i = 0
tortilla = 1
protein = 2
salsa = 3
d = {}

def Taco_Order(i):
	#print Tortilla_Choices
	#x = raw_input("> ")
	#print Tortilla_Choices['2']

	#puts tacos in a list
	taco_order.append('%s = {}' % str(i))
	i['tortilla'] = 'cornflour'
	print i
	print taco_order

#	taco_order[d['tortilla']] = '%s' % tortilla
#	taco_order[d['protein']] = '%s' % protein
#	taco_order[d['salsa']] = '%s' % salsa


#def Read_Order_Back(): #reads back entire order
#	print "\n----------RECEIPT-----------\n"
#	print taco_order[0]

#	if taco_order:
#		x = int(len(taco_order))
#		for i in taco_order:
#			x -= 1
#			print "%s" % (taco_order[x][1][0])

Taco_Order(i)
#Read_Order_Back()
