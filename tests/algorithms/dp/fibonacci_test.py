from src.algorithms.dp.fibonacci import memoization, tabulation

FIBONACCI_NUMBERS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]


def test_memoization():
    for i, n in enumerate(FIBONACCI_NUMBERS):
        assert memoization(i) == n
        assert tabulation(i) == n
