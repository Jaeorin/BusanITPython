class Person(object):
    name = None
    age = 35

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Man(Person):
    gender = 'male'


john = Person("John Doe", 40)
print(john.name)
print(john.age)

jung = Man("Jung HU", 30)
print(jung.name)
print(jung.age)
print(jung.gender)
