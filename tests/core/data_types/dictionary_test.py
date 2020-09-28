"""
1. Dictionary is an unordered collection of key-value pairs.
2. Dictionaries are optimized for retrieving data, but we must know the key to
   retrieve the value.
3. Key and value can be of any type.
"""


def test_creating_dicts():
    # empty dictionary
    my_dict = {}
    assert len(my_dict) == 0
    # dictionary with integer keys
    my_dict = {1: 'apple', 2: 'ball'}
    assert len(my_dict) == 2
    assert '{}'.format(type(my_dict)) == "<class 'dict'>"
    # dictionary with mixed keys
    my_dict = {'name': 'John', 1: [2, 4, 3]}
    assert len(my_dict) == 2
    # using dict()
    my_dict = dict({1: 'apple', 2: 'ball'})
    assert len(my_dict) == 2
    # from sequence having each item as a pair
    my_dict = dict([(1, 'apple'), (2, 'ball')])
    assert len(my_dict) == 2


def test_accessing_elements_from_dicts():
    # get vs [] for retrieving elements
    my_dict = {'name': 'Jack', 'age': 26}
    assert my_dict['name'] == 'Jack'
    assert my_dict.get('age') == 26
    assert my_dict.get('address') is None


def test_changing_and_adding_elements():
    my_dict = {'name': 'Jack', 'age': 26}
    assert my_dict['age'] == 26
    my_dict['age'] = 27
    assert my_dict['age'] == 27
    my_dict['address'] = 'Downtown'
    assert my_dict == {'address': 'Downtown', 'age': 27, 'name': 'Jack'}


def test_removing_elements_from_dicts():
    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    res = squares.pop(4)
    assert res == 16
    assert squares == {1: 1, 2: 4, 3: 9, 5: 25}
    # since 3.7 popitem() - Remove and return a (key, value) pair from the
    # dictionary. Pairs are returned in LIFO order.
    # before 3.7 Remove and return an arbitrary (key, value)
    # pair from the dictionary.
    assert squares.popitem()
    assert squares == {1: 1, 2: 4, 3: 9}
    squares.clear()
    assert len(squares) == 0
    del squares


def test_dictionary_methods():
    marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
    assert marks == {'English': 0, 'Math': 0, 'Science': 0}
    assert list(sorted(marks.keys())) == ['English', 'Math', 'Science']
    # Dictionary Built-in Functions
    squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
    assert not all(squares)
    assert any(squares)
    assert len(squares) == 6
    assert sorted(squares) == [0, 1, 3, 5, 7, 9]


def test_dictionary_comprehension():
    squares = {x: x * x for x in range(6)}
    assert squares == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    odd_squares = {x: x * x for x in range(11) if x % 2 == 1}
    assert odd_squares == {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
