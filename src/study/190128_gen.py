def iot_gen():
    print("iot_gen 1")
    yield 'a'
    print("iot_gen 2")
    print("iot_gen 2")
    yield 'b'
    print("iot_gen 3")
    print("iot_gen 3")
    print("iot_gen 3")
    yield 'c'


print(next(iot_gen()))
print(next(iot_gen()))
print(next(iot_gen()))

gen = iot_gen()
print(next(gen))
print(next(gen))
print(next(gen))

for element in [1, 2, 3]: print(element)
