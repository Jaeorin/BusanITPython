#!/usr/bin/env python

def iot_gen():
	print "iot_gen 1"
	yield 'a'
	print "iot_gen 2"
	print "iot_gen 2"
	yield 'b'
	print "iot_gen 3"
	print "iot_gen 3"
	print "iot_gen 3"
	yield 'c'

print iot_gen().next()
print iot_gen().next()
print iot_gen().next()

Nexter = iot_gen()
print Nexter.next()
print Nexter.next()
print Nexter.next()
