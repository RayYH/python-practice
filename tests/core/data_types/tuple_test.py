"""
1. Tuple is an ordered sequence of items same as a list.
2. Tuples are immutable - which means you cannot use an assignment statement
   like tuple[0]=XX.
"""


def test_creating_a_tuple():
    # Empty tuple
    my_tuple = ()
    assert len(my_tuple) == 0
    # tuple having integers
    my_tuple = (1, 2, 3)
    assert len(my_tuple) == 3
    # tuple with mixed data_types
    my_tuple = (1, "Hello", 3.4)
    assert len(my_tuple) == 3
    # nested tuple
    my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    assert len(my_tuple) == 3
    # a tuple can also be created without using parentheses.
    my_tuple = 3, 4.6, "dog"
    assert len(my_tuple) == 3
    # tuple unpacking is also possible
    a, b, c = my_tuple
    assert a == 3
    assert b == 4.6
    assert c == "dog"
    my_keywords = ("Ray", "M", 174.8, 24, "Shanghai")
    assert '{}'.format(my_keywords) == "('Ray', 'M', 174.8, 24, 'Shanghai')"
    assert my_keywords[0] == 'Ray'
    assert my_keywords[1:3] == ('M', 174.8)


def test_creating_a_tuple_with_one_element():
    # my_tuple = ("hello") has the same effect
    my_tuple = "hello"
    assert '{}'.format(type(my_tuple)) == "<class 'str'>"
    my_tuple = ("hello", )
    assert '{}'.format(type(my_tuple)) == "<class 'tuple'>"
    my_tuple = "hello",
    assert '{}'.format(type(my_tuple)) == "<class 'tuple'>"


def test_accessing_tuple_elements():
    # via index
    my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
    assert my_tuple[0] == 'p'
    assert my_tuple[5] == 't'
    assert my_tuple[-1] == 't'
    assert my_tuple[-6] == 'p'
    # nested_index
    n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    assert n_tuple[0][3] == 's'
    assert n_tuple[1][1] == 4
    my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    assert my_tuple[1:4] == ('r', 'o', 'g')
    assert my_tuple[:-7] == ('p', 'r')
    assert my_tuple[7:] == ('i', 'z')
    assert my_tuple[:] == my_tuple


def test_changing_tuple():
    my_tuple = (4, 2, 3, [6, 5])
    my_tuple[3][0] = 9
    assert my_tuple == (4, 2, 3, [9, 5])
    # Tuples can be reassigned
    my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    assert my_tuple[:] == my_tuple
    assert (1, 2, 3) + (4, 5, 6) == (1, 2, 3, 4, 5, 6)
    assert ("Repeat", ) * 3 == ('Repeat', 'Repeat', 'Repeat')


def test_deleting_tuple():
    my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    assert my_tuple[:] == my_tuple
    del my_tuple


def test_tuple_methods():
    my_tuple = (
        'a',
        'p',
        'p',
        'l',
        'e',
    )
    assert my_tuple.count('p') == 2
    assert my_tuple.index('l') == 3


def test_tuple_operations():
    my_tuple = (
        'a',
        'p',
        'p',
        'l',
        'e',
    )
    assert 'a' in my_tuple
    assert 'g' not in my_tuple
