from nose.tools import *
from ex48 import parser

#assert_raise
#bad sentence

testsentence = "princess go east"
badsentence = "princess fart burrito"

def test_peek():
	assert_equal(parser.peek("fart", [('fart','fart')]))