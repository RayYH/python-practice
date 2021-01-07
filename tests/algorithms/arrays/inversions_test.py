from src.algorithms.arrays.inversions import inversions


def test_inversions():
    assert inversions([]) == 0
    assert inversions([1, 2, 3, 4, 5, 6]) == 0
    assert inversions([2, 3, 8, 6, 1]) == 5
    assert inversions([4, 5, 6, 1, 2, 3]) == 9
    assert inversions([4, 5, 6, 1, 2, 3, 0]) == 15
    assert inversions([3, 2, 1]) == 3
    assert inversions([2, 2, 2, 2, 2, 2, 2, 2]) == 0
    assert inversions([4, 5, 6, 1, 10, 11]) == 3
