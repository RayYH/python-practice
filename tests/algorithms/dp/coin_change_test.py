from src.algorithms.dp.coin_change import minimum_coins_memoization, \
    minimum_coins_tabulation, total_combinations_tabulation
import pytest


def test_minimum_coins(m_c_case):
    assert minimum_coins_memoization(m_c_case['coins'], m_c_case['amount']) == \
           m_c_case['ans']
    assert minimum_coins_tabulation(m_c_case['coins'], m_c_case['amount']) == \
           m_c_case['ans']


def test_total_combinations(t_c_case):
    assert total_combinations_tabulation(t_c_case['coins'],
                                         t_c_case['amount']) == \
           t_c_case['ans']


@pytest.fixture(params=[
    {
        'coins': {1, 2, 5},
        'amount': 11,
        'ans': 3
    },
    {
        'coins': {1, 2, 5},
        'amount': 10,
        'ans': 2
    },
    {
        'coins': {1, 2, 5},
        'amount': 30,
        'ans': 6
    },
    {
        'coins': {1, 2, 5},
        'amount': -1,
        'ans': -1
    },
    {
        'coins': {7, 8, 9},
        'amount': 4,
        'ans': -1
    },
])
def m_c_case(request):
    yield request.param


@pytest.fixture(params=[
    {
        'coins': {1, 2, 5},
        'amount': 5,
        'ans': 4
    },
    {
        'coins': {2},
        'amount': 3,
        'ans': 0
    },
    {
        'coins': {10},
        'amount': 10,
        'ans': 1
    },
])
def t_c_case(request):
    yield request.param
