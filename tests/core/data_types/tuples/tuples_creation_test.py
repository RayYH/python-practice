def test_empty_tuple():
    assert len(()) == 0


def test_same_data_types():
    my_tuple = (1, 2, 3)
    assert len(my_tuple) == 3


def test_mixed_data_types():
    my_tuple = (1, "Hello", 3.4)
    assert len(my_tuple) == 3


def test_nested_data_types():
    my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    assert len(my_tuple) == 3


def test_without_parentheses():
    my_tuple = 3, 4.6, "dog"
    assert len(my_tuple) == 3
