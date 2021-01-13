from src.helper.ioh import to_string, captured_output
from math import sqrt


# for in loop
def sum_of_numbers(numbers):
    sum_num = 0
    for val in numbers:
        sum_num += val
    return sum_num


def test_sum_of_numbers():
    assert sum_of_numbers(range(1, 4)) == 6
    assert sum_of_numbers([1.1, 2.2, 3.3]) == 6.6


# for in with range method
def frac(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result


def test_frac():
    x = [1, 2, 3, 4]
    y = [1, 2, 6, 24]
    for a, b in zip(x, y):
        assert frac(a) == b


def test_for_loop_with_else():
    with captured_output() as (out, err):
        digits = [0, 1, 5]
        for i in digits:
            print(i, end=" ")
        else:
            print("No items left.", end=" ")
    assert to_string(out) == "0 1 5 No items left."
