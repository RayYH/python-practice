def test_delete_tuple():
    my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    assert my_tuple[:] == my_tuple
    del my_tuple


def test_modify_tuple():
    my_tuple = (4, 2, 3, [6, 5])
    my_tuple[3][0] = 9
    assert my_tuple == (4, 2, 3, [9, 5])


def test_repeat_tuple():
    assert ("Repeat", ) * 3 == ('Repeat', 'Repeat', 'Repeat')


def test_accessing_tuple_elements():
    my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
    assert my_tuple[0] == 'p'
    assert my_tuple[5] == 't'
    assert my_tuple[-1] == 't'
    assert my_tuple[-6] == 'p'
    assert my_tuple[1:4] == ('e', 'r', 'm')
    assert my_tuple[:-4] == ('p', 'e')
    assert my_tuple[4:] == ('i', 't')
    assert my_tuple[:] == my_tuple


def test_unpacking_tuple():
    my_tuple = 3, 4.6, "dog"
    a, b, c = my_tuple
    assert a == 3
    assert b == 4.6
    assert c == "dog"


def test_convert_tuple_to_string():
    my_keywords = ("Ray", "M", 174.8, 24, "Shanghai")
    assert '{}'.format(my_keywords) == "('Ray', 'M', 174.8, 24, 'Shanghai')"
