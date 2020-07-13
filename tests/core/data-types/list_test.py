def test_lists():
    # empty list
    my_list = []
    assert len(my_list) == 0
    # list of integers
    my_list = [1, 2, 3]
    assert len(my_list) == 3
    # list with mixed data types
    my_list = [1, "Hello", 3.4]
    assert len(my_list) == 3
    # nested list
    my_list = ["mouse", [8, 4, 6], ['a']]
    assert len(my_list) == 3
    my_list = ['p', 'r', 'o', 'b', 'e']
    #  0  1  2  3  4
    # -5 -4 -3 -2 -1
    assert my_list[0] == 'p'
    assert my_list[2] == 'o'
    assert my_list[4] == 'e'
    assert my_list[-1] == 'e'
    assert my_list[-5] == 'p'
    n_list = ["Happy", [2, 0, 1, 5]]
    assert n_list[0][1] == 'a'
    assert n_list[1][3] == 5


def test_slicing_list():
    # slice lists
    my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
    # including left but exclude right
    # elements 3rd to 5th
    assert my_list[2:5] == ['o', 'g', 'r']
    # elements beginning to 4th
    assert my_list[:-5] == ['p', 'r', 'o', 'g']
    # elements 6th to end
    assert my_list[5:] == ['a', 'm', 'i', 'z']
    # elements beginning to end
    assert my_list[:] == my_list


def test_modify_list():
    # Correcting mistake values in a list
    odd = [2, 4, 6, 8]
    # change the 1st item
    odd[0] = 1
    assert odd == [1, 4, 6, 8]
    odd[1:4] = [3, 5, 7]
    assert odd == [1, 3, 5, 7]
    odd.append(9)
    assert odd == [1, 3, 5, 7, 9]
    odd.extend([11, 13, 15])
    assert odd == [1, 3, 5, 7, 9, 11, 13, 15]
    odd = odd + [17, 19]
    assert odd == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert ["re"] * 3 == ["re", "re", "re"]
    # Demonstration of list insert() method
    odd = [1, 9]
    odd.insert(1, 3)
    assert odd == [1, 3, 9]
    odd[2:2] = [5, 7]
    assert odd == [1, 3, 5, 7, 9]
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    # delete one item
    del my_list[2]
    assert my_list == ['p', 'r', 'b', 'l', 'e', 'm']
    # delete multiple items
    del my_list[1:5]
    assert my_list == ['p', 'm']
    # delete entire list
    del my_list
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    my_list.remove('p')
    assert my_list == ['r', 'o', 'b', 'l', 'e', 'm']
    res = my_list.pop(1)
    assert res == 'o'
    assert my_list == ['r', 'b', 'l', 'e', 'm']
    res = my_list.pop()
    assert res == 'm'
    assert my_list == ['r', 'b', 'l', 'e']
    my_list.clear()
    assert my_list == []
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    my_list[2:3] = []
    assert my_list == ['p', 'r', 'b', 'l', 'e', 'm']
    my_list[2:5] = []
    assert my_list == ['p', 'r', 'm']


def test_list_methods():
    # Python list methods
    my_list = [3, 8, 1, 6, 0, 8, 4]
    assert my_list.index(8) == 1
    assert my_list.count(8) == 2
    my_list.sort()
    assert my_list == [0, 1, 3, 4, 6, 8, 8]
    my_list.reverse()
    assert my_list == [8, 8, 6, 4, 3, 1, 0]


def test_list_comprehension():
    pow2 = [2 ** x for x in range(10)]
    assert pow2 == [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    odd = [x for x in range(20) if x % 2 == 1]
    assert odd == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    lists = [x + y for x in ['Python ', 'C '] for y in ['Language', 'Programming']]
    assert lists == ['Python Language', 'Python Programming', 'C Language', 'C Programming']


def test_list_other_operations():
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    assert 'p' in my_list
    assert 'a' not in my_list
    assert 'c' not in my_list
