"""
I. You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1. You may assume that you have an
infinite number of each kind of coin.

II. You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that
amount. You may assume that you have infinite number of each kind of coin.

@see https://leetcode.com/problems/coin-change
@see https://leetcode.com/problems/coin-change-2
"""
from typing import Set, Dict
import sys


def minimum_coins_memoization(coins: Set[int], amount: int) -> int:
    memo = {}
    return minimum_coins_memo(coins, amount, memo)


def minimum_coins_memo(coins: Set[int], amount: int, memo: Dict) -> int:
    # check memo
    if amount in memo:
        return memo.get(amount)

    # base case and condition check
    if amount == 0:
        return 0

    if amount <= 0:
        return -1

    # recursive
    res = sys.maxsize
    for coin in coins:
        sub_ans = minimum_coins_memo(coins, amount - coin, memo)
        # no solution
        if sub_ans == -1:
            continue
        # if has solution
        res = min(res, sub_ans + 1)

    # update memo (no solution when initial value not changed) and return
    memo[amount] = res if res != sys.maxsize else -1
    return memo[amount]


def minimum_coins_tabulation(coins: Set[int], amount: int) -> int:
    # condition check
    if amount < 0:
        return -1

    # init table
    tables = [sys.maxsize] * (amount + 1)

    # base case in table
    tables[0] = 0

    # update table via formula
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin < 0:
                continue
            tables[i] = min(tables[i], tables[i - coin] + 1)

    # return stored value in tables (no solution when initial value not changed)
    return tables[amount] if tables[amount] != sys.maxsize else -1
