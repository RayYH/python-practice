from ctypes import CDLL, c_float
from src.helper.path import get_test_resources_dir


def add_int(a, b):
    adder = CDLL(get_test_resources_dir() + '/c/add.so')
    return adder.add_int(a, b)


def add_float(a, b):
    adder = CDLL(get_test_resources_dir() + '/c/add.so')
    x = c_float(a)
    y = c_float(b)
    adder.add_float.restype = c_float
    return adder.add_float(x, y)


if __name__ == '__main__':
    print("Sum of 4 and 5 = " + str(add_int(4, 5)))
    print("Sum of 5.5 and 4.1 = ", str(add_float(5.5, 4.1)))
