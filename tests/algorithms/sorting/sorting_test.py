import pytest
from src.algorithms.sorting.helper import is_sorted, count_equals
from src.algorithms.sorting.quick_sort import quick_sort
from src.algorithms.sorting.selection_sort import selection_sort
from src.algorithms.sorting.insertion_sort import insertion_sort, \
    recursive_insertion_sort, insertion_sort_scanning_via_binary_search
from src.algorithms.sorting.merge_sort import merge_sort, merge_sort_part
from src.algorithms.sorting.bubble_sort import bubble_sort
from src.algorithms.sorting.heap_sort import heap_sort


def sorting_assert(arr, algorithm, *args):
    unsorted_list = arr.copy()
    sorted_list = algorithm(arr, *args)
    assert is_sorted(sorted_list) and count_equals(sorted_list, unsorted_list)


def test_quick_sort(unsorted):
    sorting_assert(unsorted, quick_sort)


def test_selection_sort(unsorted):
    sorting_assert(unsorted, selection_sort)


def test_insertion_sort(unsorted):
    sorting_assert(unsorted, insertion_sort)


def test_recursive_insertion_sort(unsorted):
    sorting_assert(unsorted, recursive_insertion_sort, len(unsorted))


def test_insertion_sort_scanning_via_binary_search(unsorted):
    sorting_assert(unsorted, insertion_sort_scanning_via_binary_search)


def test_bubble_sort(unsorted):
    sorting_assert(unsorted, bubble_sort)


def test_heap_sort(unsorted):
    sorting_assert(unsorted, heap_sort)


def test_merge_sort(unsorted):
    sorting_assert(unsorted, merge_sort)
    sorting_assert(unsorted, merge_sort_part, 0, len(unsorted))


@pytest.fixture(params=[[], [1], [1, 5], [3, 3], [3, 2, 4], [2, 2, 2, 2, 2, 2],
                        [4, 1, 3, 2, 9, 1],
                        [23, 11, 9, 12321, 12, 3, 1, 90, 99999],
                        ["a", "d", "e", "z", "b", "h", "z"]])
def unsorted(request):
    yield request.param
