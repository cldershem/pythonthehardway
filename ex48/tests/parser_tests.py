from nose.tools import *
from ex48 import parser

#assert_raise
#bad sentence

word_list = ["princess", "go", "east"]
bad_word_list = ["taco", "fart", "burrito"]
error = "ERROR!"
expecting = ["subect", "verb", "object"]


def test_peek():
	#if "x" is passed to parser.peek, is result "expected result"?
	assert_equal(parser.peek([word_list]), ("princess"))
	try:
		assert_equal(parser.peek([bad_word_list]), ("princess"))
	except AssertionError:
		return error

def test_match():
	assert_equal(parser.peek([bad_word_list]), ("princess"))
