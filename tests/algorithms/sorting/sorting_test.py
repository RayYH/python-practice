import pytest
from src.algorithms.sorting.helper import is_sorted
from src.algorithms.sorting.quick_sort import quick_sort
from src.algorithms.sorting.selection_sort import selection_sort
from src.algorithms.sorting.insertion_sort import insertion_sort, \
    recursive_insertion_sort, insertion_sort_scanning_via_binary_search
from src.algorithms.sorting.merge_sort import merge_sort
from src.algorithms.sorting.bubble_sort import bubble_sort


def test_quick_sort(unsorted):
    assert is_sorted(quick_sort(unsorted))


def test_selection_sort(unsorted):
    assert is_sorted(selection_sort(unsorted))


def test_insertion_sort(unsorted):
    assert is_sorted(insertion_sort(unsorted))


def test_recursive_insertion_sort(unsorted):
    assert is_sorted(recursive_insertion_sort(unsorted, len(unsorted)))


def test_insertion_sort_scanning_via_binary_search(unsorted):
    assert is_sorted(insertion_sort_scanning_via_binary_search(unsorted))


def test_bubble_sort(unsorted):
    assert is_sorted(bubble_sort(unsorted))


def test_merge_sort(unsorted):
    assert is_sorted(merge_sort(unsorted))


@pytest.fixture(params=[[3, 2, 4], [23, 11, 9, 12321, 12, 3, 1, 90, 99999],
                        ["a", "d", "e", "z", "b", "h", "z"]])
def unsorted(request):
    yield request.param
