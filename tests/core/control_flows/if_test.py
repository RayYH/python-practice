from src.core.control_flows.if_statement import greater_than_3, greater_than_5, equals


def test_greater_than_3():
    assert greater_than_3(4)
    assert not greater_than_3(1)


def test_greater_than_5():
    assert greater_than_5(6)
    assert not greater_than_5(4)


def test_equals():
    assert equals(5, 5) == 0
    assert equals(10, 9) == 1
    assert equals(9, 10) == -1
