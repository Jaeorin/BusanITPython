import datetime


def deco_test(test_arg):
    def iot_time_data():
        print("==========================")
        print(datetime.datetime.now())
        test_arg()
        print(datetime.datetime.now())

    return iot_time_data


def iot_function1():
    print("iot function1 start")


def iot_function2():
    print("iot function2 start")


def iot_function3():
    print("iot function3 start")


def iot_function4():
    print("iot function4 start")


deco_test_1 = deco_test(iot_function1)
deco_test_1()
deco_test_2 = deco_test(iot_function2)
deco_test_2()
deco_test_3 = deco_test(iot_function3)
deco_test_3()
deco_test_4 = deco_test(iot_function4)
deco_test_4()
