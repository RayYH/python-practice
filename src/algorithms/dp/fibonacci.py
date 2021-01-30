MAX_NUM = 100
NIL = -1
MEMO = [NIL] * MAX_NUM


def memoization(n: int) -> int:
    if MEMO[n] == NIL:
        if n <= 1:
            MEMO[n] = n
        else:
            MEMO[n] = memoization(n - 1) + memoization(n - 2)

    return MEMO[n]


def tabulation(n: int) -> int:
    if n <= 1:
        return n

    tables = [-1] * (n + 1)
    tables[0:2] = [0, 1]

    for i in range(2, n + 1):
        tables[i] = tables[i - 1] + tables[i - 2]

    return tables[n]
