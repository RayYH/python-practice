def test_in_operator():
    my_tuple = ('a', 'p', 'p', 'l', 'e')
    assert 'a' in my_tuple
    assert 'g' not in my_tuple


def test_plus_operator():
    tuple1 = ('a', )
    tuple2 = ('b', )
    assert tuple1 + tuple2 == ('a', 'b')
