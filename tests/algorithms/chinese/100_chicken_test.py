from src.algorithms.chinese.a_hundred_of_chicken import get_solutions


def test_100_chicken():
    assert get_solutions() == [
        {
            '5': 0,
            '3': 25,
            '1': 75
        },
        {
            '5': 4,
            '3': 18,
            '1': 78
        },
        {
            '5': 8,
            '3': 11,
            '1': 81
        },
        {
            '5': 12,
            '3': 4,
            '1': 84
        },
    ]
