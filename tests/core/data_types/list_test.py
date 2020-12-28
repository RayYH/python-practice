import pytest


def test_lists_creation():
    empty_list = []
    assert not empty_list
    squares = [1, 4, 9, 16, 25]
    assert squares
    # list with mixed data types
    mine = ["Ray", 24]
    assert mine


def test_lists_can_be_indexed_and_sliced():
    squares = [1, 4, 9, 16, 25]
    assert squares[0] == 1
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]
    assert squares[:] == squares


def test_lists_concatenation():
    squares = [1, 4, 9, 16, 25]
    assert squares + [36, 49, 64] == [1, 4, 9, 16, 25, 36, 49, 64]


def test_lists_are_mutable():
    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 4 ** 3
    assert cubes == [1, 8, 27, 64, 125]


def test_assignment_to_slices():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # replace some values
    letters[2:5] = ['C', 'D', 'E']
    assert letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    # now remove them
    letters[2:5] = []
    assert letters == ['a', 'b', 'f', 'g']
    # clear the list by replacing all the elements with an empty list
    letters[:] = []
    assert not letters


def test_length_of_lists():
    letters = ['a', 'b', 'c', 'd']
    assert len(letters) == 4


def test_nest_lists():
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    assert x == [['a', 'b', 'c'], [1, 2, 3]]
    assert x[0] == ['a', 'b', 'c']
    assert x[0][1] == 'b'


def test_convert_lists_to_strings():
    mixed_list = ["a", 1, 3.14, 1]
    assert '{}'.format(mixed_list) == "['a', 1, 3.14, 1]"
    cities = ["Beijing", "Tokyo", "New York", "London", "Paris"]
    assert '{}'.format(cities) == \
           "['Beijing', 'Tokyo', 'New York', 'London', 'Paris']"


def test_convert_lists_to_sets():
    mixed_list = ["a", 1, 3.14, 1]
    assert set(mixed_list) == {1, 3.14, 'a'}


def test_in_operator():
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    assert 'p' in my_list
    assert 'a' not in my_list


def test_copy_lists():
    b = a = [1, 2, 3]
    b[0] = 4
    assert a == [4, 2, 3]
    c = a[:]
    c[0] = 5
    assert a == [4, 2, 3]
    assert c == [5, 2, 3]


def test_add_item_to_lists():
    cubes = [1, 8, 27, 64, 125]
    assert cubes
    # add new items at the end of the list
    cubes.append(216)
    cubes.append(7 ** 3)
    assert cubes == [1, 8, 27, 64, 125, 216, 343]
    # add new items at specified index
    odd = [1, 5]
    odd.insert(1, 3)
    assert odd == [1, 3, 5]


def test_remove_items_from_lists_via_index():
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    # delete one item
    del my_list[2]
    assert my_list == ['p', 'r', 'b', 'l', 'e', 'm']
    # delete multiple items
    del my_list[1:5]
    assert my_list == ['p', 'm']
    # clear list
    my_list.clear()
    assert my_list == []
    # delete entire list - my_list not exists anymore
    del my_list


def test_remove_items_from_lists_via_value():
    my_list = ['r'] * 3
    with pytest.raises(ValueError):
        my_list.remove('value_does_not_exists')
    # remove first occurrence of value
    my_list.remove('r')
    assert my_list == ['r', 'r']
    my_list = ['r', 'p', 'r', 'p']
    my_list.remove('p')
    assert my_list == ['r', 'r', 'p']


def test_remove_items_via_pop_method():
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    # item at index 2
    item = my_list.pop(2)
    assert item == 'o'
    assert my_list == ['p', 'r', 'b', 'l', 'e', 'm']
    # last item
    item = my_list.pop()
    assert item == 'm'
    assert my_list == ['p', 'r', 'b', 'l', 'e']


def test_extend_lists():
    odd = [1, 3, 5, 7, 9]
    # use extend method
    odd.extend([11, 13, 15])
    assert odd == [1, 3, 5, 7, 9, 11, 13, 15]
    # use + operator
    odd = odd + [17, 19]
    assert odd == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def test_repeated_lists():
    assert ["re"] * 3 == ["re", "re", "re"]


def test_lists_methods():
    my_list = [3, 8, 1, 6, 0, 8, 4]
    assert my_list.index(8) == 1
    assert my_list.count(8) == 2
    my_list.sort()
    assert my_list == [0, 1, 3, 4, 6, 8, 8]
    my_list.reverse()
    assert my_list == [8, 8, 6, 4, 3, 1, 0]
    # use ::-1 to reverse again
    assert my_list[::-1] == [0, 1, 3, 4, 6, 8, 8]


def test_lists_generators():
    pow2 = [2 ** x for x in range(10)]
    assert pow2 == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    odd = [x for x in range(20) if x % 2 == 1]
    assert odd == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    lists = [
        x + y for x in ['Python ', 'C '] for y in ['Language', 'Programming']
    ]
    assert lists == [
        'Python Language', 'Python Programming', 'C Language', 'C Programming'
    ]
