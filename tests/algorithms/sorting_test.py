import pytest
from src.algorithms.sorting.quick_sort import quick_sort


def is_sorted(collection):
    return all(collection[i] <= collection[i + 1] for i in range(len(collection) - 1))


def test_quick_sort(unsorted):
    assert is_sorted(quick_sort(unsorted))


@pytest.fixture(params=[[23, 11, 9, 12321, 12, 3, 1, 90], ["a", "d", "e", "z", "b", "h"]])
def unsorted(request):
    yield request.param
