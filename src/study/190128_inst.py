class Iot(object):
    name = None

    def __init__(self, name_arg):
        print("init call")
        name = name_arg


obj1 = Iot("iot object 1")
print(obj1.name)

obj2 = Iot("iot object 2")
print(obj2.name)
