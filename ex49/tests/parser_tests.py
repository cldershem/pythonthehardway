from nose.tools import *
from ex49 import parser
from ex49 import lexicon

sentence = 'princess go east'
verb_sentence = 'run go east'
obj_sentence = 'the east'
bad_sentence = 'taco fart burrito'

def test_Sentence():
	tuple_list = lexicon.scan(sentence)
	s = parser.Sentence(tuple_list[0],tuple_list[1],tuple_list[2])
	assert_equal(s.subject, 'princess')
	assert_equal(s.verb, 'go')
	assert_equal(s.object, 'east')
	word_list = [s.subject, s.verb, s.object]
	assert_equal(word_list, (['princess', 'go', 'east']))

def test_peek():
	word_list = lexicon.scan(sentence)
	assert_equal(parser.peek(word_list), 'noun')
	assert_equal(parser.peek(None), None)

def test_match():
	word_list = lexicon.scan(sentence)
	assert_equal(parser.match(word_list, 'noun'), ('noun', 'princess'))

def test_skip():
	word_list = lexicon.scan(sentence)
	assert_equal(word_list, [('noun','princess'), ('verb','go'),
													('direction', 'east')])
	parser.skip(word_list, 'noun')
	assert_equal(word_list, [('verb','go'), ('direction', 'east')])

def test_parse_verb():
	word_list = lexicon.scan(verb_sentence)
	assert_equal(parser.parse_verb(word_list), ('verb', 'go'))
	word_list = lexicon.scan(sentence)
	assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_object():
	word_list = lexicon.scan(sentence)
	assert_equal(parser.parse_object(word_list), ('noun', 'princess'))
	word_list = lexicon.scan(obj_sentence)
	assert_equal(parser.parse_object(word_list), ('direction', 'east'))
	assert_raises(parser.ParserError, parser.parse_object, word_list)

#def test_parse_subject():
#		word_list = lexicon.scan(verb_sentence)
#		subj = ('noun', 'princess')
#		print subj
#		print word_list
#		s = parser.parse_subject(word_list, subj)
#		assert_equal((s), ('go','east'))

def test_parse_sentence():
	tuple_list = lexicon.scan(sentence)
	s = parser.Sentence(tuple_list[0],tuple_list[1],tuple_list[2])
	word_list = s.subject, s.verb, s.object
	assert_equal(word_list, ('princess', 'go', 'east'))

	tuple_list = lexicon.scan(verb_sentence)
	s = parser.Sentence(tuple_list[0],tuple_list[1],tuple_list[2])
#	word_list = s.subject, s.verb, s.object
	assert_equal(s,('player', 'go', 'east'))

	word_list = lexicon.scan('bad sentence')
	assert_raises(parser.ParserError, parser.parse_sentence, word_list)

#https://github.com/bitsai/book-exercises/blob/4807253c31e878770532e943fb28d39a04cc3a93/Learn%20Python%20the%20Hard%20Way/projects/ex49/tests/ex49_tests.py
