from src.algorithms.mathematical.freivald import freivald


def test_freivald():
    a = [[1, 1], [1, 1]]
    b = [[1, 1], [1, 1]]
    c = [[2, 2], [2, 2]]
    assert freivald(a, b, c)
    c = [[2, 3], [2, 2]]
    assert not freivald(a, b, c)
    a = [[2, 1], [4, 3]]
    b = [[1, 2], [1, 0]]
    c = [[3, 4], [7, 8]]
    assert freivald(a, b, c)
