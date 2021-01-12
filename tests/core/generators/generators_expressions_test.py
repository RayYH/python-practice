def test_generator_expressions():
    my_list = [1, 2, 3, 6]
    assert [x ** 2 for x in my_list] == [1, 4, 9, 36]
    generator = (x ** 2 for x in my_list)
    assert '{}'.format(generator).startswith('<generator object')
    assert next(generator) == 1
    assert next(generator) == 4
    assert next(generator) == 9
    assert next(generator) == 36


def test_generator_expressions_as_parameters():
    my_list = [1, 2, 3, 6]
    assert sum(x ** 2 for x in my_list) == 50
    assert max(x ** 2 for x in my_list) == 36
    x_vec = [10, 20, 30]
    y_vec = [7, 5, 3]
    assert sum(x * y for x, y in zip(x_vec, y_vec)) == 260
