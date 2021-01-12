"""
Technically speaking, a Python iterator object must implement two special
methods, __iter__() and __next__(), collectively called the iterator protocol.
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
        """
         __iter__() method returns an object with a __next__() method.
        """
        self.n = 0
        return self

    def __next__(self):
        """
        __next__() method accesses elements in the container one at a time.
        """
        if self.n <= self.max_nums:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            # tells the for loop to terminate
            raise StopIteration


def test_power_two():
    numbers = PowTwo(3)
    i = iter(numbers)
    assert next(i) == 1
    assert next(i) == 2
    assert next(i) == 4
    assert next(i) == 8


class OddNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


def test_odd_numbers():
    a = iter(OddNumbers())
    start = 1
    for i in range(30):
        assert next(a) == start + 2 * i
