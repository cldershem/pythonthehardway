from random import randint, shuffle, sample

def Shuffled_Beers():
		list_of_beers = [
									"Coors Light",
									"Budweiser",
									"Miller 64",
									"Sierra Nevada Pale Ale",
									"Darklord"
									]
		shuffled_beers = [''.join(sample(beer, len(beer))) for 
											beer in list_of_beers]
		return shuffled_beers

print Shuffled_Beers()
