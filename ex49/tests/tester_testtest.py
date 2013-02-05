directions = ['north', 'south', 'east', 'west', 'down', 'up', 'right', 'back']
verbs = ['go', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it', 'stop']
nouns = ['door', 'bear', 'princess', 'cabinet']

word_list = ["princess", "go", "east"]
bad_word_list = ["taco", "fart", "burrito"]
error = "ERROR!"
expecting = ["subect", "verb", "object"]

class ParserError(Exception):
	pass

class Sentence(object):

	def __init__(self, subject, verb, object):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subect[1]
		self.verb = verb[1]
		self.object = object[1]


def peek(word_list):
	print "peek"
	print word_list
	if word_list:
		print word_list[0]
		word = word_list[0]
		print word[0]
		return word[0]
	else:
		return None


def match(word_list, expecting):
	print "match"
	if word_list:
		print word_list
		word = word_list.pop(0)
		print word

		if word[0] == expecting:
			print word
			return word
		else:
			return None

	else:
		return None

def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)

def pars_verb(word_list):
	skip(word_list, 'stop')

	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next.")

def parse_object(word_list):
	skip(word_list, 'stop')
	next = peek(word_list)

	if next == 'noun':
		return match(word_list, 'noun')
	if next == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list, subj):
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subj, verb, obj)

def parse_sentence(word_list):
	skip(word_list, 'stop')

	start = peek(word_list)

	if start == 'noun':
		subj == match(word_list, 'noun')
		return parse_subject(word_list, subj)
	elif start == 'verb':
		# assume the subject is the player then
		return parse_subject(word_list, ('noun', 'player'))
	else:
		raise ParserError("Must start with subject, obeject, or verb not: %s" % start)

#peek(word_list)
match(word_list, expecting)