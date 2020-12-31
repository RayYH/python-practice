import pytest


def test_add():
    my_set = set()
    my_set.add(1)
    assert my_set == {1}


def test_pop():
    my_set = {1, 3, 4, 5, 6}
    res = my_set.pop()
    assert res == 1
    assert my_set == {3, 4, 5, 6}


def test_update():
    my_set = {1, 3, 4, 5, 6}
    another_set = {3, 4, 5, 8, 9}
    my_set.update(another_set)
    assert my_set == {1, 3, 4, 5, 6, 8, 9}


def test_clear():
    my_set = {1, 3, 4, 5, 6}
    my_set.clear()
    assert not my_set


def test_remove():
    my_set = {1, 3, 4, 5, 6}
    my_set.remove(1)
    assert my_set == {3, 4, 5, 6}
    with pytest.raises(KeyError):
        my_set.remove(0)


def test_copy():
    my_set = {1, 3, 4, 5, 6}
    my_set_1 = my_set
    my_set_2 = my_set.copy()
    my_set.remove(1)
    assert my_set == my_set_1 == {3, 4, 5, 6}
    assert my_set_2 == {1, 3, 4, 5, 6}


def test_difference_update():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    a.difference_update(b)
    assert a == {1, 2, 3}


def test_discard():
    my_set = {1, 3, 4, 5, 6}
    my_set.discard(1)
    assert my_set == {3, 4, 5, 6}
    my_set.discard(0)  # No error


def test_intersection_update():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    a.intersection_update(b)
    assert a == {4, 5}


def test_isdisjoint():
    my_set_1 = {1, 2, 3}
    my_set_2 = {3, 4, 5}
    my_set_3 = {5, 6, 7}
    assert not my_set_1.isdisjoint(my_set_2)
    assert not my_set_2.isdisjoint(my_set_3)
    assert my_set_1.isdisjoint(my_set_3)


def test_issubset():
    my_set_1 = {1, 2}
    my_set_2 = {1, 2, 3}
    assert my_set_1.issubset(my_set_2)


def test_issuperset():
    my_set_1 = {1, 2}
    my_set_2 = {1, 2, 3}
    assert my_set_2.issuperset(my_set_1)


def test_symmetric_difference_update():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    a.symmetric_difference_update(b)
    assert a == {1, 2, 3, 6, 7, 8}
