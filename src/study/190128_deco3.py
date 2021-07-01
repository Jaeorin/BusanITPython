import datetime


def deco_test(test_arg):
    def iot_time_data():
        print("==========================")
        print(datetime.datetime.now())
        test_arg()
        print(datetime.datetime.now())

    return iot_time_data


@deco_test
def iot_function1():
    print("iot function1 start")


@deco_test
def iot_function2():
    print("iot function2 start")


@deco_test
def iot_function3():
    print("iot function3 start")


@deco_test
def iot_function4():
    print("iot function4 start")


iot_function1()
iot_function2()
iot_function3()
iot_function4()
