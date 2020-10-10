from src.core.control_flows.if_statement \
    import greater_than_3, greater_than_5, equals
from random import randint


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
