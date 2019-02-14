
class Person(object):
    name = None
    age = 35
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def think(self):
        print "I'm thinking..."

john = Person("John Doe", 40)
print john.name
print john.age
john.think()