def test_in_operator():
    my_set = set("apple")
    assert 'a' in my_set
    assert 'z' not in my_set


def test_union_operation():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    assert a | b == {1, 2, 3, 4, 5, 6, 7, 8}
    assert a.union(b) == {1, 2, 3, 4, 5, 6, 7, 8}
    assert b.union(a) == {1, 2, 3, 4, 5, 6, 7, 8}


def test_intersection_operation():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    assert a & b == {4, 5}
    assert a.intersection(b) == {4, 5}
    assert b.intersection(a) == {4, 5}


def test_difference_operation():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    assert a - b == {1, 2, 3}
    assert a.difference(b) == {1, 2, 3}
    assert b - a == {6, 7, 8}
    assert b.difference(a) == {6, 7, 8}


def test_symmetric_difference_operation():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    assert a ^ b == {1, 2, 3, 6, 7, 8}
    assert a.symmetric_difference(b) == {1, 2, 3, 6, 7, 8}
    assert b.symmetric_difference(a) == {1, 2, 3, 6, 7, 8}
