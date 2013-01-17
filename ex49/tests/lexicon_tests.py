from nose.tools import *
from ex49 import lexicon

def test_directions():
	#if "north" passed to lexicon.scan, is result "direction, north"?
	assert_equal(lexicon.scan("north"), [('direction','north')])
	#if "north south east" passed to lexicon.scan, is result list?
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
												('direction', 'south'),
												('direction', 'east')])

def test_verbs():
	assert_equal(lexicon.scan("go"), [('verb', 'go')])
	result = lexicon.scan("go kill eat")
	assert_equal(result, [('verb', 'go'),
												('verb', 'kill'),
												('verb', 'eat')])

def test_stops():
	assert_equal(lexicon.scan("the"), [('stop', 'the')])
	result = lexicon.scan("the in of")
	assert_equal(result, [('stop', 'the'),
												('stop', 'in'),
												('stop', 'of')])

def test_nouns():
	assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
	result = lexicon.scan("bear princess")
	assert_equal(result, [('noun', 'bear'),
													('noun', 'princess')])

def test_numbers():
	assert_equal(lexicon.scan("1234"), [('number', 1234)])
	result = lexicon.scan("3 91234")
	assert_equal(result, [('number', 3),
												('number', 91234)])

def test_errors():
	assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
	result = lexicon.scan("bear IAS princess")
	assert_equal(result, [('noun', 'bear'),
												('error', 'IAS'),
												('noun', 'princess')])

#https://github.com/bitsai/book-exercises/blob/4807253c31e878770532e943fb28d39a04cc3a93/Learn%20Python%20the%20Hard%20Way/projects/ex49/tests/ex49_tests.py
