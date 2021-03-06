from src.algorithms.misc.two_sum import two_sum, exists


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_exists():
    assert exists([2, 11, 7, 15], 9)
    assert exists([3, 2, 4], 6)
    assert not exists([3, 2, 4, 6], 99)
    assert not exists([3, 2, 4, 6], 4)
