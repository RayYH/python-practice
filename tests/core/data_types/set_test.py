"""
1. Set is an unordered collection of unique items.
2. Items in a set are not ordered, indexing has no meaning.
"""


def test_creating_sets():
    my_set = {1, 2, 3}
    assert len(my_set) == 3
    my_set = {1.0, "Hello", (1, 2, 3)}
    assert len(my_set) == 3
    my_set = {1, 2, 3, 4, 3, 2}
    assert my_set == {1, 2, 3, 4}
    my_list = [1, 2, 3, 2]
    my_set = set(my_list)
    assert my_set == {1, 2, 3}
    assert '{}'.format(type({})) == "<class 'dict'>"
    assert '{}'.format(type(set())) == "<class 'set'>"


def test_modifying_a_set():
    my_set = {1, 3}
    my_set.add(2)
    assert my_set == {1, 2, 3}
    my_set.update([2, 3, 4])
    assert my_set == {1, 2, 3, 4}
    my_set.update([4, 5, 7], {1, 6, 8})
    assert my_set == {1, 2, 3, 4, 5, 6, 7, 8}


def test_removing_elements_from_a_set():
    my_set = {1, 3, 4, 5, 6}
    my_set.discard(4)
    assert my_set == {1, 3, 5, 6}
    my_set.remove(6)
    assert my_set == {1, 3, 5}
    # here use remove will cause an error
    my_set.discard(2)
    assert my_set == {1, 3, 5}
    my_set = set("HelloWorld")
    res = my_set.pop()
    assert res in "HelloWorld"
    my_set.pop()
    assert len(my_set) == 5
    my_set.clear()
    assert my_set == set()


def test_set_operations():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    assert a | b == {1, 2, 3, 4, 5, 6, 7, 8}
    assert a.union(b) == {1, 2, 3, 4, 5, 6, 7, 8}
    assert b.union(a) == {1, 2, 3, 4, 5, 6, 7, 8}
    assert a & b == {4, 5}
    assert a.intersection(b) == {4, 5}
    assert b.intersection(a) == {4, 5}
    assert a - b == {1, 2, 3}
    assert a.difference(b) == {1, 2, 3}
    assert b - a == {6, 7, 8}
    assert b.difference(a) == {6, 7, 8}
    # Set Symmetric Difference
    assert a ^ b == {1, 2, 3, 6, 7, 8}
    assert a.symmetric_difference(b) == {1, 2, 3, 6, 7, 8}
    assert b.symmetric_difference(a) == {1, 2, 3, 6, 7, 8}
    my_set = set("apple")
    assert 'a' in my_set
    assert 'z' not in my_set
