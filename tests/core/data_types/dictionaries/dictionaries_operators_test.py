def test_in_operator():
    my_dict = {'jack': 4098, 'guido': 4127, 'irv': 4127}
    assert 'guido' in my_dict
    assert 'invalid' not in my_dict
