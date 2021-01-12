"""
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments are given.

Base 0 means to interpret the base from the string as an integer literal.
"""
import pytest


def test_empty_int_invocation_returns_zero():
    assert int() == 0
    assert int() == 0


def test_base_zero():
    assert 0b100 == 4
    with pytest.raises(ValueError):
        # invalid literal for int() with base 10: '0b100'
        assert int('0b100') == 4
    assert int('0b100', base=0) == 4
    assert int('0o100', base=0) == 64


def test_int_iterators():
    """
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.
    """
    inf = iter(int, 1)
    assert inf.__next__() == 0
    assert inf.__next__() == 0
    assert inf.__next__() == 0
    assert next(inf) == 0
