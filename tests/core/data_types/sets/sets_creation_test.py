def test_declaration():
    my_set = {1, 2, 3}
    assert len(my_set) == 3
    my_set = {1.0, "Hello", (1, 2, 3)}
    assert len(my_set) == 3


def test_automatic_remove_duplicates():
    my_set = {1, 2, 3, 4, 3, 2}
    assert my_set == {1, 2, 3, 4}
    my_list = [1, 2, 3, 2]
    my_set = set(my_list)
    assert my_set == {1, 2, 3}
