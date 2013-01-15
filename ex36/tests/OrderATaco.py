from sys import exit

#lists
Help_Choices = ['tacos', 'drink', 'none']
Other_Choices = ['bathroom', 'none']
Tortilla_Choices = ['corn', 'flour']
Protein_Choices = ['beef', 'pork', 'fish', 'shrimp', 'bean']
Salsa_Choices = ['pico de gallo', 'roja', 'verde', 'none']
Drink_Choices = ['horchata', 'tamarindo', 'jarritos']
Jarritos_Choices = ['fruit punch', 'lime', 'hibiscus', 'guava', 'mandarin']

taco_order = []
taco_order1 = []
#taco_order2 = []
#taco_order3 = []
#taco_order4 = []
#taco_order5 = []

chip_order = []
drink_order = []

#May I help you?
def Can_I_Help():
	print "What can I do for you today?"
	print Help_Choices
	next = raw_input("> ")

	if next == "tacos": #order tacos
		Taco_Order()
	elif next == "drink": #order only drink
		Drink_Order()
	elif next == "none": #don't order anything
		Other_Order()
	else:
		print "You apparently don't understand the choices."
		Slap()

	return next

def Taco_Order(): #order taco
	print "How many tacos would you like?"
	try :
		qty = int(raw_input("> ")) 
	except ValueError:
		Slap()
	if qty == 0:
		Slap()
	if qty >= 25:
		print "Sorry, you'll need ot call ahead for that amount."
		Slap()
	#if qty > 1:
	print "Would you like all of your tacos the same? (y/n)"
	same = raw_input("> ")
	if same == "y":
		count = qty
	elif same == "n":
		count = 1
	while count <= qty:
		if same == "n":
			print "\tTaco %r" % count

		print "What kind of tortilla?"
		print Tortilla_Choices
		tortilla = raw_input("> ")

		if tortilla not in Tortilla_Choices:
			Slap()

		print "What kind of protein?"
		print Protein_Choices
		protein = raw_input("> ")

		if protein not in Protein_Choices:
			Slap()

		print "What kind of salsa?"
		print Salsa_Choices
		salsa = raw_input("> ")

		if salsa == "none":
			print "Wuss"
		elif salsa not in Salsa_Choices:
			Slap()
		count += 1
		taco_order.append(tortilla)
		taco_order.append(protein)
		taco_order.append(salsa)
		taco_order1 = list(taco_order)
		print taco_order1

	print "Would you like chips?"
	chips = raw_input("> (y/n)")

	if chips == "y":
		print "What kind of salsa?"
		print Salsa_Choices
		chip_salsa = raw_input("> ")

		if chip_salsa == "none":
			print "Wuss"
		elif chip_salsa not in Salsa_Choices:
			Slap()
		chip_order.append(chip_salsa)

	elif chips == "n":
		chips = "no"
		chip_salsa = "no"
	else:
		Slap()

	print "Would you like a drink?"
	next = raw_input("> (y/n)")

	if next == "y": #sends you to Drink_Order()
		Drink_Order()
	elif next == "n":
		drink = "nothing"
	else:
		Slap()

def Read_Order_Back(): #reads back entire order
	if taco_order1:	
		print "You ordered a %r taco with a %r tortilla and %r salsa." % (taco_order1[1],taco_order1[0],taco_order1[2])
		if chip_order:
			print "You ordered chips with %s salsa." % (chip_order[0])
	if drink_order:
		print "You ordered %s to drink." % (drink_order[0])
	print "You're lucky that we aren't charging today."
	print "Thank you for your patronage."

def Drink_Order(): #can be used by itself or with taco order
	print "What would you like to drink?"
	print Drink_Choices
	drink = raw_input("> ")
	if drink not in Drink_Choices:
		Slap()
	if drink == "jarritos":
		print "Which flavor?"
		print Jarritos_Choices
		jarritos = raw_input("> ")
		if jarritos not in Jarritos_Choices:
			Slap()
		else:
			drink = "%s jarritos" % (jarritos)
	drink_order.append(drink)

def Other_Order(): #choices if you're not ordering
	print "What else can I do for you?"
	print Other_Choices
	next = raw_input("> ")

	if next == "bathroom":
		print "Squaters: down the hall and to the left."
		print "Shooters: there's an alley out back."
		exit(0)
	else:
		Slap()

def Slap(): #if you exit like this you are an ass.
	print "Quit wasting my time."
	print "<--------- Slaps you."
	print "Good bye."
	exit(0)

Can_I_Help()
Read_Order_Back()
