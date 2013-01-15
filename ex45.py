from sys import exit
from random import randint, shuffle, sample

#Scenes

class Scene(object):
	
	def enter(self):
		print "This hasn't been configured yet."
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n----------\n"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Freezer(Scene):

	def enter(self):
		print "You wake up in a cold, dark room.  There are boxes"
		print "of beer surrounding you.  You need to get out."
		print "You see a faint light at one end of the room."
		print "Upon closer inscpection you see that it has a keypad."
		print "What do you do?"
		print "1. Guess the keypad code?"
		print "2. Get drunk on mystery beer?"
		choice = raw_input("> ")

		if choice == "1":
			code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9),)
			print "You must guess the keycode."
			#print code #take this out of live game
			guess = raw_input("keycode: (hint ***)> ")
			guesses = 0

			while guess != code and guesses < 9:
				print "You are WRONG! %d guesses left." % (9 - guesses)
				guesses += 1

				if guesses == 3:
					print "HINT!"
					print "%s**" % code[0]

				elif guesses == 6:
					print "HINT!"
					print "%s*" % code[0:2]

				elif guesses == 9:
					print "HINT!"
					print "%s" % code[0:3]

				guess = raw_input("keycode: (hint ***)> ")

			if guess == code:
				print "The door seal breaks, letting in more light."
				print "You can now see that you have dodged the biggest bullet of all."
				print "The cases of beer around you are Coors Light."
				print "Had you chosen to stay and drink them......"
				print "......You would have surely died of bad taste."
				return 'Hallway'

			else:
				print "You suck at guessing codes."
				print "You eventually freeze to death."
				return 'Death'

		elif choice == "2":
			print "You open a case of mystery beer and take out a bottle."
			print "You open the bottle and put it to your lips."
			print "Upon tasting the brew you realize you've made a mistake."
			print "You are locked in the Shitty Beer Cooler."
			print "You are drinking Coors Light and eventually die of bad taste."
			return 'Death'
		else:
			print "You apparently don't understand the choices."
			return 'Freezer'

class Hallway(Scene):

#figure out how to make it take another variable

	def enter(self):
		print "You walk into a short hallway with two doors."
		print "1. Left Door"
		print "2. Right Door"
		choice = raw_input("> ")

		if choice == "1":
			print "You walk towards the door and open it."
			return 'Closet'

		elif choice == "2":
			print "You walk towards the door and open it."
			return 'Office'

		else:
			print "You apparently don't understand the choices."
			return 'Hallway'

class Closet(Scene):

	def enter(self):
		print "You enter a dark, dark room.  The door slams behind you."
		print "You feel around.  Shelves, boxes, a couple of wooden sticks."
		print "You are feeling clostraphobic.  What do you do?"
		print "1. Open a box?"
		print "2. Turn around and open the door?"
		choice = raw_input("> ")

		if choice == "1":
			print "You open a box and try to look inside."
			print "It is too dark to see, but you get a strange feeling."
			print "Your soul is being sucked out of you."
			return 'Death'		

		if choice == "2":
			print "You turn around and after struggling to find the handle"
			print "you realize it was never locked in the first place."
			print "You walk through the hallway and go into the other door."
			return 'Office'

		else:
			print "You apparently don't understand the choices."
			return 'Closet'

class Office(Scene):

	def enter(self):
		print "You enter an office.  There are papers scattered everywhere."
		print "On the far end of the room there is a locked door."
		print "What do you do?"
		print "1: Pick up the phone and call your lifeline?"
		print "2: Attempt to pick the lock from items you find around?"
		choice = raw_input("> ")

		if choice == "1":
			print "You pick up the phone to try and dial Ron Swanson."
			print "You cannot figure out how to get an outside line."
			print "You eventually die from boredom."
			return 'Death'

		elif choice == "2":
			print "You find a paperclip, a bobby pin, and a stick of gum."
			print "From your years of watching MacGyver you have learned"
			print "a thing or two."
			print "The door opens."
			return 'ComputerRoom'

		else:
			print "You apparently don't understand the choices."
			return 'Office'

class ComputerRoom(Scene):

	def enter(self):
		print "You enter a brightly lit, loud, chilly room."
		print "There are computers all around you.  Most of them with BSODs."
		print "You see a door on one side of the room, but it is clearly locked"
		print "with some high level security stuff."
		print "You see one open terminal and you sit down in front of it."
		print "It is asking for the root password."
		password = "1337"
		guess = raw_input("password: (hint ****)>")

		guesses = 0

		while guess != password and guesses < 9:
			print "You are WRONG!  %d guesses left." % (9 - guesses)
			guesses += 1

			if guesses == 3:
				print "HINT!"
				print "%s***" % password[0]

			elif guesses == 6:
				print "HINT!"
				print "%s**" % password[0:2]

			elif guesses == 9:
				print "HINT!"
				print "%s*" % password[0:3]

			guess = raw_input("password: (hint ****)")

		if guess == password:
			print "You realize that their IT guy is either 13 or an asshole."
			print "Either way you don't care, you've just h4X0r3d the mainframe."
			print "You quickly unlock the door."
			return 'Bar'
		else:
			print "The terminal begins flashing red and prints out:"
			print "\'-------YOU SUCK!  I PWN YOU!  BOOM HEADSHOT!-------\'"
			print "You realize you're trying to hack an moron."
			return 'ComputerRoom'

class Bar(Scene):

	def shuffled_beers(self):
		list_of_beers = [
										"coors light",
										"budweiser",
										"miller 64",
										"sierra nevada pale ale",
										"darklord"
										]
		shuffled_beer_list = [''.join(sample(beer, len(beer))) for 
											beer in list_of_beers]
		return shuffled_beer_list	

	def enter(self):
		print "You walk into the back of a bar.  After all of that you could "
		print "really use a beer so you sit down on a barstool."
		print "The bartender walks up."
		print "I'll have an Alpha King."
		print "\n\tBartender: You have got some balls coming back in here."
		print "\tI'll make you a deal, I'll serve you the beer if can "
		print "\ttell me the best beer in this list."
		print "\nThe bartender grabs a napkin, writes on it and hands it to you."
		print "The napkin reads:"
		print '\n'.join(self.shuffled_beers())
		print "What is the best beer?"
		guess = raw_input("> ")
		guesses = 0

		while guess != "darklord" and guesses < 9:
			print "You are WRONG!  %d guesses left." % (9 - guesses)
			guesses += 1
			guess = raw_input("> ")

		if guess == "darklord":
			print "\n\tBartender:  You aren't as drunk as I thought.  Here is your"
			print "\tAlpha King."
			print "..."
			print "..."
			print "..."
			print "6 Alpha Kings later..."
			print "Bartender:  You frackin' asshat.  I must have been a fool"
			print "\tto let you drink here again.  GET OUT!!!!"
			return 'Street'

		else:
			print "You suck at this this.  You really do."
			return 'Death'
			

class Street(Scene):

	def enter(self):
		print "You are pushed out the door and stumble onto the sidewalk."
		print "You look down and realize that you may have urinated on yourself."
		print "You reach in your pocket and realize you still have your wallet."
		print "You realize that even though you got kicked out of that bar"
		print "you didn't have to pay.  You win!"
		print "YAY!"
		
		exit(0)

class Death(Scene):

	def enter(self):
		print "You suck."
		exit(0)

class Map(object):

	scenes = {
		'Freezer': Freezer(),
		'Hallway': Hallway(),
		'Closet': Closet(),
		'Office': Office(),
		'ComputerRoom': ComputerRoom(),
		'Bar': Bar(),
		'Street': Street(),
		'Death': Death()
		}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('Freezer')
a_game = Engine(a_map)
a_game.play()
