import pytest
from src.algorithms.arrays.squares_of_a_sorted_array import \
    distinct_count, all_squares


def test_distinct_count(dc_case):
    assert distinct_count(dc_case['nums']) == dc_case['ans']


def test_all_squares(as_case):
    assert all_squares(as_case['nums']) == as_case['ans']


@pytest.fixture(params=[{
    'nums': [],
    'ans': 0
}, {
    'nums': [-3, -2, -1, 0],
    'ans': 4
}, {
    'nums': [-3, -2, -2, -2, -1, 0],
    'ans': 4
}, {
    'nums': [-1, -1, -1, 1, 1, 1, 1],
    'ans': 1
}, {
    'nums': [-3, -3, -3, -3],
    'ans': 1
}, {
    'nums': [-3, -2, 1, 2, 3, 4, 9, 9, 9, 11],
    'ans': 6
}])
def dc_case(request):
    yield request.param


@pytest.fixture(params=[{
    'nums': [],
    'ans': []
}, {
    'nums': [-3, -2, -1, 0],
    'ans': [0, 1, 4, 9]
}, {
    'nums': [-3, -2, -2, -2, -1, 0],
    'ans': [0, 1, 4, 4, 4, 9]
}, {
    'nums': [-1, -1, -1, 1, 1, 1, 1],
    'ans': [1, 1, 1, 1, 1, 1, 1]
}, {
    'nums': [-3, -3, -3, -3],
    'ans': [9, 9, 9, 9]
}, {
    'nums': [-3, -2, 1, 2, 3, 4, 9, 9, 9, 11],
    'ans': [1, 4, 4, 9, 9, 16, 81, 81, 81, 121]
}])
def as_case(request):
    yield request.param
