#!/usr/bin/env python

class iot(object):
    name = None
    def __init__(self, name_arg):
        print "init call"
        self.name = name_arg

obj1 = iot("iot 1")
print obj1.name

obj2 = iot("iot 2")
print obj2.name