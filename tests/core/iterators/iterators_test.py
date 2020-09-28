"""
Technically speaking, a Python iterator object must implement
two special methods, __iter__() and __next__(),
collectively called the iterator protocol.
An object is called iterable if we can get an iterator from it.
Most built-in containers in Python like: list, tuple, string etc. are iterables.
"""


class PowTwo:
    """
    Class to implement an iterator of powers of two
    """

    def __init__(self, max_nums=0):
        self.max_nums = max_nums

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max_nums:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


class InfIter:
    """
    Infinite iterator to return all odd numbers
    """

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


def test_iter():
    my_list = [4, 7, 0, 3]
    # get an iterator using iter()
    my_iter = iter(my_list)
    # iterate through it using next()
    assert next(my_iter) == 4
    assert next(my_iter) == 7
    # next(obj) is same as obj.__next__()
    assert my_iter.__next__() == 0
    assert my_iter.__next__() == 3
    # create an iterator object from that iterable
    iter_obj = iter(my_list)
    # use for loop
    for element in my_list:
        assert element >= 0
    # infinite loop
    while True:
        try:
            # get the next item
            element = next(iter_obj)
            assert element >= 0
            # do something with element
        except StopIteration:
            # if StopIteration is raised, break from loop
            break


def test_pass_two():
    # create an object
    numbers = PowTwo(3)
    # create an iterable from the object
    i = iter(numbers)
    # Using next to get to the next iterator element
    assert next(i) == 1
    assert next(i) == 2
    assert next(i) == 4
    assert next(i) == 8


def test_infinite_iterators():
    assert int() == 0
    inf = iter(int, 1)
    assert inf.__next__() == 0
    assert next(inf) == 0
    a = iter(InfIter())
    start = 1
    for i in range(30):
        assert next(a) == start + 2 * i
