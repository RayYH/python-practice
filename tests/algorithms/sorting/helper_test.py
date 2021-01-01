from src.algorithms.sorting.helper import is_sorted


def test_is_sorted():
    assert is_sorted([])
    assert is_sorted([1, 2])
    assert is_sorted(['a', 'e'])
