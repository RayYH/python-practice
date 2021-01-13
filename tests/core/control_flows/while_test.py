from src.helper.ioh import captured_output, to_string


# while loop
def sum_from_1_to_n(n):
    num_sum = 0
    i = 1
    while i <= n:
        num_sum += i
        i += 1
    return num_sum


def test_sum_from_1_to_n():
    assert sum_from_1_to_n(10) == 55
    assert sum_from_1_to_n(3) == 6


# while loop with else
def while_loop_with_else():
    counter = 0
    while counter < 3:
        print("Inside loop", end=" ")
        counter += 1
    else:
        print("Inside else", end=" ")


def test_while_loop_with_else():
    with captured_output() as (out, err):
        while_loop_with_else()
    assert to_string(out) == "Inside loop " * 3 + "Inside else"


def fibonacci_series(n=10):
    a, b = 0, 1
    while a < n:
        print(a, end="") if a == n - 1 else print(a, end=" ")
        a, b = b, a + b


def test_fibonacci_series():
    with captured_output() as (out, err):
        fibonacci_series()
    assert to_string(out) == "0 1 1 2 3 5 8"
