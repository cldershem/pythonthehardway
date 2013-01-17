directions = ['north', 'south', 'east', 'west', 'down', 'up', 'right', 'back']
verbs = ['go', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it', 'stop']
nouns = ['door', 'bear', 'princess', 'cabinet']

def scan(words):

	words = words.split()
	result = []

	for word in words:
		if word in directions:
			result.append(('direction', word))
		elif word in verbs:
			result.append(('verb', word))
		elif word in stops:
			result.append(('stop', word))
		elif word in nouns:
			result.append(('noun', word))
		elif word.isdigit():
			result.append(('number', convert_number(word)))
		else:
			result.append(('error', word))
	return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
