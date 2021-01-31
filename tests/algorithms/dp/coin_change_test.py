from src.algorithms.dp.coin_change import minimum_coins_memoization, \
    minimum_coins_tabulation
import pytest


def test_minimum_coins(case):
    assert minimum_coins_memoization(case['coins'], case['amount']) == \
           case['ans']
    assert minimum_coins_tabulation(case['coins'], case['amount']) == \
           case['ans']


@pytest.fixture(params=[
    {'coins': {1, 2, 5}, 'amount': 11, 'ans': 3},
    {'coins': {1, 2, 5}, 'amount': 10, 'ans': 2},
    {'coins': {1, 2, 5}, 'amount': 30, 'ans': 6},
    {'coins': {1, 2, 5}, 'amount': -1, 'ans': -1},
    {'coins': {7, 8, 9}, 'amount': 4, 'ans': -1},
])
def case(request):
    yield request.param
