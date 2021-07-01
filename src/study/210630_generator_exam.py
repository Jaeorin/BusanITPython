def generator_send():
    print("-=-=-=-=-=-= Generator Start =-=-=-=-=-=-")
    received_value = 0 # 먼저 변수를 지정해줍니다.
    received_value2 = 0 # 먼저 변수를 지정해줍니다.
    received_value3 = 0
    while True:
        received_value = yield "send" #1
        print("received_value = ")
        print(received_value)  #3
        received_value2 = yield "send2" #1
        print("received_value2 = ")
        print(received_value2)  #3
        yield received_value * received_value2 #2
    print("-=-=-=-=-=-= Generator End =-=-=-=-=-=-")

gen = generator_send()
print("")
print("-=-=-=-=-=-= print Start =-=-=-=-=-=-")
print(next(gen)) #1
print(gen.send(2)) #2
print(gen.send(6))

print(gen.send(5)) #1
print(gen.send(2)) #2
print(gen.send(6))
print("-=-=-=-=-=-= print End =-=-=-=-=-=-")