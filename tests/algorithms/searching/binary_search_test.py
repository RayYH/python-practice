from src.algorithms.sorting.helper import is_sorted
from src.algorithms.searching.binary_search import binary_search, \
    recursive_binary_search


def test_binary_search():
    sorted_list = [1, 3, 5, 7, 9]
    assert is_sorted(sorted_list)
    assert binary_search(sorted_list, 3) == 1
    assert not binary_search(sorted_list, -1)


def test_recursive_binary_search():
    sorted_list = [1, 3, 5, 7, 9]
    assert is_sorted(sorted_list)
    assert recursive_binary_search(sorted_list, 3) == 1
    assert not recursive_binary_search(sorted_list, -1)
