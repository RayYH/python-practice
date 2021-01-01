import pytest
from src.algorithms.sorting.helper import is_sorted
from src.algorithms.sorting.quick_sort import quick_sort
from src.algorithms.sorting.selection_sort import selection_sort
from src.algorithms.sorting.insertion_sort import insertion_sort
from src.algorithms.sorting.merge_sort import merge_sort


def test_quick_sort(unsorted):
    assert is_sorted(quick_sort(unsorted))


def test_selection_sort(unsorted):
    assert is_sorted(selection_sort(unsorted))


def test_insertion_sort(unsorted):
    assert is_sorted(insertion_sort(unsorted))


def test_merge_sort(unsorted):
    assert is_sorted(merge_sort(unsorted))


@pytest.fixture(params=[[23, 11, 9, 12321, 12, 3, 1, 90],
                        ["a", "d", "e", "z", "b", "h"]])
def unsorted(request):
    yield request.param
