#!/usr/bin/env python

def handler():
	print "Initialize Handler"
	while True:
		value = (yield)
		print "Received %s" % value
