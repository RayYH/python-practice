"""
Python generators are a simple way of creating iterators.

Simply speaking, a generator is a function that returns an object (iterator)
which we can iterate over (one value at a time).
"""


def one_two_three():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n


def test_one_two_three():
    gen = one_two_three()
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3
    i = 1
    for item in one_two_three():
        assert i == item
        i += 1
