from sys import exit

#known errors
#if tacos the same only prints one

#todo
#make lists use numbers

#lists
Help_Choices = ['tacos', 'drink', 'chips', 'none']
Other_Choices = ['bathroom', 'none']
Tortilla_Choices = ['corn', 'flour']
Protein_Choices = ['beef', 'pork', 'fish', 'shrimp', 'bean']
Salsa_Choices = ['pico de gallo', 'roja', 'verde', 'none']
Drink_Choices = ['horchata', 'tamarindo', 'jarritos']
Jarritos_Choices = ['fruit punch', 'lime', 'hibiscus', 'guava', 'mandarin']

taco_order = []
chip_order = []
drink_order = []

#May I help you?
def Can_I_Help():
	print "What can I do for you today?"
	print Help_Choices
	next = raw_input("> ")

	if next == "tacos": #order tacos
		Order_Order()
	elif next == "drink": #order only drink
		Drink_Order()
	elif next == "chips": #order only chips
		Chip_Order()
	elif next == "none": #don't order anything
		Other_Order()
	else:
		Slap()

def Order_Order(): #order taco
	print "How many tacos would you like?"
	try :
		qty = int(raw_input("> ")) 
	except ValueError:
		Slap()
	if qty <= 0:
		Slap()
	elif qty >= 25:
		print "Sorry, you'll need ot call ahead for that amount."
		Slap()
	elif qty == 1:
		taco_num = 0
		i = 0
		Taco_Order(i)
	else:
		print "Would you like all of your tacos the same? (y/n)"
		same = raw_input("> ")
		if same == "y":
			taco_num = 0
			i = 0
			Taco_Order(i)
		elif same == "n":
			for i in xrange(qty):
				taco_num = "Taco"+str(i+1)
				print "\t %s" % (taco_num)
				Taco_Order(i)
	Chips_Or_Drink()

def Taco_Order(i):
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
	#puts tacos in a list
	taco_order.append([i])
	taco_order[i].append([tortilla,protein,salsa])

def Chips_Or_Drink():
	print "Would you like chips?"
	chips = raw_input("> (y/n)")

	if chips == "y":
		Chip_Order()

	elif chips == "n":
		print "You're missing out."
	else:
		Slap()

	print "Would you like a drink?"
	next = raw_input("> (y/n)")

	if next == "y": #sends you to Drink_Order()
		Drink_Order()
	elif next == "n":
		print "Too bad, our horchata is fresh."
	else:
		Slap()

def Drink_Order(): #can be used by itself or with taco order
	print "What would you like to drink?"
	print Drink_Choices
	drink = raw_input("> ")
	if drink not in Drink_Choices:
		Slap()
	elif drink == "jarritos":
		print "Which flavor?"
		print Jarritos_Choices
		jarritos = raw_input("> ")
		if jarritos not in Jarritos_Choices:
			Slap()
		else:
			drink = "%s jarritos" % (jarritos)
	drink_order.append(drink)

def Chip_Order():
	print "What kind of salsa for your chips?"
	print Salsa_Choices
	chip_salsa = raw_input("> ")
	if chip_salsa == "none":
		print "Wuss"
		chip_salsa = "no"
	elif chip_salsa not in Salsa_Choices:
		Slap()
	chip_order.append(chip_salsa)

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

def Read_Order_Back(): #reads back entire order
	print "\n----------RECEIPT-----------\n"

	if taco_order:
		x = int(len(taco_order))
		for i in taco_order:
			x -= 1
			print "You ordered %s taco(s) with %s tortilla(s) and %s salsa." % (taco_order[x][1][1],taco_order[x][1][0],taco_order[x][1][2])
	if chip_order:
		print "You ordered chips with %s salsa." % (chip_order[0])
	if drink_order:
		print "You ordered %s to drink." % (drink_order[0])
	print "You're lucky that we aren't charging today."
	print "Thank you for your patronage."
	print "\n---------END RECEIPT--------\n"

def Slap(): #if you exit like this you are an ass.
	print "You apparently don't understand the choices."
	print "Quit wasting my time."
	print "<--------- Slaps you."
	print "Good bye."
	exit(0)

Can_I_Help()
Read_Order_Back()
