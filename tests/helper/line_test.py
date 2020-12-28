from src.helper.line import star, dash, NUM
from src.helper.ioh import captured_output


@star
def print_star():
    print("do something")


@dash
def print_dash():
    print("do something")


def test_star():
    with captured_output() as (out, err):
        print_star()
    assert out.getvalue().strip() == "*" * NUM + "\ndo something\n" + "*" * NUM


def test_dash():
    with captured_output() as (out, err):
        print_dash()
    assert out.getvalue().strip() == "-" * NUM + "\ndo something\n" + "-" * NUM
