from src.algorithms.arrays.maximum_subarray \
    import divide_and_conquer_solution, kadane_algorithm_solution, \
    brute_force_solution
import pytest


def test_maximum_subarray_via_divide_and_conquer(case):
    assert divide_and_conquer_solution(case['nums']) == \
           case['maximum']


def test_maximum_subarray(case):
    assert kadane_algorithm_solution(case['nums']) == case['maximum']


def test_brute_force_solution(case):
    assert brute_force_solution(case['nums']) == case['maximum']


@pytest.fixture(params=[{
    'nums': [-2147483647],
    'maximum': -2147483647
}, {
    'nums': [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    'maximum': 6
}, {
    'nums': [-1],
    'maximum': -1
}, {
    'nums': [0],
    'maximum': 0
}, {
    'nums': [1],
    'maximum': 1
}, {
    'nums': [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    'maximum': 6
}])
def case(request):
    yield request.param
