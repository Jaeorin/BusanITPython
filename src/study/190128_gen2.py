def handler():
    # print("Initialize Handler")
    while True:
        value = yield "output"
        print("Received %s" % value)
        yield value * 3 #2


listener = handler()
print("")
# print(listener.send(1))
# print(listener.send(None))
print(next(listener))
print(listener.send(1))
print(listener.send(2))
print(listener.send(1))
print(next(listener))
