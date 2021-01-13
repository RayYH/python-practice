from random import randint


# if
def greater_than_3(number):
    if number > 3:
        return True
    return False


# if-else
def greater_than_5(number):
    if number > 5:
        return True
    else:
        return False


# if-elif-else
def equals(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def compare_to_zero(number):
    if number >= 0:
        if number == 0:
            return 0
        else:
            return 1
    else:
        return -1


def test_greater_than_3():
    assert greater_than_3(randint(4, 10))
    assert not greater_than_3(randint(1, 3))


def test_greater_than_5():
    assert greater_than_5(randint(6, 10))
    assert not greater_than_5(randint(1, 5))


def test_equals():
    assert equals(5, 5) == 0
    assert equals(10, 9) == 1
    assert equals(9, 10) == -1
