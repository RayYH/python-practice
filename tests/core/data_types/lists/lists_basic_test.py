def test_lists_can_be_indexed_and_sliced():
    squares = [1, 4, 9, 16, 25]
    assert squares[0] == 1
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]
    assert squares[:] == squares


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


def test_convert_lists_to_strings():
    mixed_list = ["a", 1, 3.14, 1]
    assert '{}'.format(mixed_list) == "['a', 1, 3.14, 1]"
    cities = ["Beijing", "Tokyo", "New York", "London", "Paris"]
    assert '{}'.format(cities) == \
           "['Beijing', 'Tokyo', 'New York', 'London', 'Paris']"


def test_convert_lists_to_sets():
    mixed_list = ["a", 1, 3.14, 1]
    assert set(mixed_list) == {1, 3.14, 'a'}


def test_repeated_lists():
    assert ["re"] * 3 == ["re", "re", "re"]


def test_delete_item():
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    assert a
    del a[0]
    assert a == [1, 66.25, 333, 333, 1234.5]
    del a[2:4]
    assert a == [1, 66.25, 1234.5]
    del a[:]
    assert len(a) == 0
