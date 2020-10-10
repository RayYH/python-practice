from src.core.control_flows.for_statement \
    import sum_of_numbers, frac, is_prime, get_gcd_and_lcm
from src.helper.io import to_string, captured_output


def test_sum():
    # not range(1, 3), instead: range(0, 4): 1+2+3 = 6
    assert sum_of_numbers(range(0, 4)) == 6
    assert sum_of_numbers([1.1, 2.2, 3.3]) == 6.6


def test_frac():
    assert frac(1) == 1
    assert frac(2) == 2
    assert frac(3) == 6
    assert frac(4) == 24


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)


def test_for_range():
    """
    python does not support (i = 0; i < 10; i++) syntax
    but you can use for-range syntax to make it
    """
    with captured_output() as (out, err):
        # (i = 0; i < 10; i++)
        for i in range(0, 10, 1):
            # 0 1 2 3 4 5 6 7 8 9
            print("{}".format(i), end=" ")
    assert to_string(out) == "0 1 2 3 4 5 6 7 8 9"
    with captured_output() as (out, err):
        # (i = 0; i < 10; i = i+2)
        for i in range(0, 10, 2):
            # 0 2 4 6 8
            print("{}".format(i), end=" ")
    assert to_string(out) == "0 2 4 6 8"
    with captured_output() as (out, err):
        # discard the index value
        for _ in range(0, 10, 1):
            print("{}".format('*'), end="")
    assert to_string(out) == "*" * 10


def test_range():
    assert '{}'.format(type(range(10))) == "<class 'range'>"
    assert '{}'.format(list(range(10))) == "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
    assert '{}'.format(list(range(2, 8))) == "[2, 3, 4, 5, 6, 7]"
    assert '{}'.format(list(range(2, 20, 3))) == "[2, 5, 8, 11, 14, 17]"
    with captured_output() as (out, err):
        genre = ['pop', 'rock', 'jazz']
        # iterate over the list using index
        for i in range(len(genre)):
            print(genre[i], end=" ")
    assert to_string(out) == "pop rock jazz"


def test_for_loop_with_else():
    with captured_output() as (out, err):
        digits = [0, 1, 5]
        for i in digits:
            print(i, end=" ")
        # when loop is done
        else:
            print("No items left.", end=" ")
        # program to display student's marks from record
        student_name = 'Ray'
        marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
        for student in marks:
            if student == student_name:
                print(marks[student], end=" ")
                break
        else:
            print('No entry with that name found.', end=" ")
    assert to_string(
        out) == "0 1 5 No items left. No entry with that name found."


def test_yield_gcd_and_lcm():
    res = get_gcd_and_lcm(12, 18)
    assert res['gcd'] == 6
    assert res['lcm'] == 36
    res = get_gcd_and_lcm(5, 7)
    assert res['gcd'] == 1
    assert res['lcm'] == 35
