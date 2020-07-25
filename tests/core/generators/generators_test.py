"""
Python generators are a simple way of creating iterators.
Simply speaking, a generator is a function that returns an object (iterator)
 which we can iterate over (one value at a time).
"""


# A simple generator function
def my_gen():
    n = 1
    # Generator function contains yield statements
    yield n

    n += 1
    yield n

    n += 1
    yield n


def test_my_gen():
    a = my_gen()
    assert next(a) == 1
    assert next(a) == 2
    assert next(a) == 3
    i = 1
    for item in my_gen():
        assert i == item
        i += 1


def test_generator_expression():
    # Initialize the list
    my_list = [1, 2, 3, 6]
    # square each item use list comprehension
    list_ = [x ** 2 for x in my_list]
    # same thing can be done using a generator expression
    # generator expressions are surrounded by parenthesis ()
    generator = (x ** 2 for x in my_list)
    assert list_ == [1, 4, 9, 36]
    assert '{}'.format(generator).startswith('<generator object')
    assert next(generator) == 1
    assert next(generator) == 4
    assert next(generator) == 9
    assert next(generator) == 36
    # Generator expressions can be used as function arguments.
    assert sum(x ** 2 for x in my_list) == 50
    assert max(x ** 2 for x in my_list) == 36
