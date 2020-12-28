from src.helper.ioh import captured_output, to_string
from functools import reduce, lru_cache


# Enumerate() method adds a counter to an iterable and returns
# it in a form of enumerate object.
def test_enumerate():
    fruits = ['apple', 'orange', 'banana']
    greeting = 'hello'
    e1 = enumerate(fruits)
    # changing start index to 2 from 0
    e2 = enumerate(greeting, 2)
    assert '{}'.format(type(e1)) == "<class 'enumerate'>"
    assert '{}'.format(type(e2)) == "<class 'enumerate'>"
    assert list(e1) == [(0, 'apple'), (1, 'orange'), (2, 'banana')]
    assert list(e2) == [(2, 'h'), (3, 'e'), (4, 'l'), (5, 'l'), (6, 'o')]
    with captured_output() as (out, err):
        # MUST use enumerate(fruits) instead of e1
        for ele in enumerate(fruits):
            print(ele)
        for count, ele in enumerate(greeting, 2):
            print(count, ele)
    assert (to_string(out)) == '''(0, 'apple')
(1, 'orange')
(2, 'banana')
2 h
3 e
4 l
5 l
6 o'''


def multiply(x):
    return x * x


def add(x):
    return x + x


def test_map():
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, items))
    assert squared == [1, 4, 9, 16, 25]
    funcs = [multiply, add]
    values = []
    for i in range(5):
        values.append(list(map(lambda x: x(i), funcs)))
    assert values == [[0, 0], [1, 2], [4, 4], [9, 6], [16, 8]]


def test_filter():
    number_list = range(-5, 5)
    less_than_zero = list(filter(lambda x: x < 0, number_list))
    assert less_than_zero == [-5, -4, -3, -2, -1]


def test_reduce():
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    assert product == 24


@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# Function caching allows us to cache the return values of a function depending
# on the arguments. It can save time when an I/O bound function is periodically
# called with the same arguments.
def test_lru_cache():
    assert [fib(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # un-cache the return values
    fib.cache_clear()
    assert [fib(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
