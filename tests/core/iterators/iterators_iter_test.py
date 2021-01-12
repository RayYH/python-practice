def test_next_methods():
    my_list = [4, 7, 0, 3]
    my_iter = iter(my_list)
    assert next(my_iter) == 4
    assert next(my_iter) == 7
    assert my_iter.__next__() == 0
    assert my_iter.__next__() == 3


def test_loop_iterators():
    my_list = [4, 7, 0, 3]
    iter_obj = iter(my_list)

    # ues for loop
    for element in my_list:
        assert element >= 0

    # use while
    while True:
        try:
            element = next(iter_obj)
            assert element >= 0
        except StopIteration:
            break
