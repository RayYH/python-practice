import pytest
from src.algorithms.arrays.powers_of_sorted_array import solution


def test_solution(case):
    assert solution(case['nums']) == case['ans']


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
def case(request):
    yield request.param
