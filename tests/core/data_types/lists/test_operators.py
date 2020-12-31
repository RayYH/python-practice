def test_in_operator():
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
    assert 'p' in my_list
    assert 'a' not in my_list


def test_plus_operator():
    my_list1 = ['p', 'r', 'o']
    my_list2 = ['b', 'l', 'e', 'm']
    assert my_list1 + my_list2 == ['p', 'r', 'o', 'b', 'l', 'e', 'm']
