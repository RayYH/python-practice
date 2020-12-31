from math import pi


def test_lists_creation():
    empty_list = []
    assert not empty_list
    squares = [1, 4, 9, 16, 25]
    assert squares
    # list with mixed data types
    mine = ["Ray", 24]
    assert mine


def test_create_squares():
    squares1 = []
    for x in range(10):
        squares1.append(x ** 2)
    squares2 = list(map(lambda y: y ** 2, range(10)))
    squares3 = [x ** 2 for x in range(10)]
    assert squares1 == squares2 == squares3


def test_create_combs():
    combs1 = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs1.append((x, y))
    combs2 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert combs1 == combs2


def test_creation_examples():
    vec = [-4, -2, 0, 2, 4]
    assert [x * 2 for x in vec] == [-8, -4, 0, 4, 8]
    assert [x for x in vec if x >= 0] == [0, 2, 4]
    assert [abs(x) for x in vec] == [4, 2, 0, 2, 4]
    fresh_fruits = [' banana', ' loganberry ', 'passion fruit ']
    assert [weapon.strip() for weapon in fresh_fruits] == \
           ['banana', 'loganberry', 'passion fruit']
    assert [(x, x ** 2) for x in range(6)] == \
           [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert [num for elem in vec for num in elem] == \
           [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert [str(round(pi, i)) for i in range(1, 6)] == \
           ['3.1', '3.14', '3.142', '3.1416', '3.14159']
