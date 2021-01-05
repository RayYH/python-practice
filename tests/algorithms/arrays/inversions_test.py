from src.algorithms.arrays.inversions import number_of_inversions


def test_inversions():
    assert number_of_inversions([]) == 0
    assert number_of_inversions([1, 2, 3, 4, 5, 6]) == 0
    assert number_of_inversions([2, 3, 8, 6, 1]) == 5
    assert number_of_inversions([4, 5, 6, 1, 2, 3]) == 9
    assert number_of_inversions([4, 5, 6, 1, 2, 3, 0]) == 15
