from src.helper.io import captured_output, to_string
from src.core.decorators.decorators import \
    ordinary, divide, printer


def test_ordinary():
    with captured_output() as (out, err):
        ordinary()
    assert to_string(out) == 'I got decorated\nI am ordinary'


def test_divide():
    with captured_output() as (out, err):
        divide(4, 2)
    assert to_string(out) == 'I am going to divide 4 and 2\n2.0'
    with captured_output() as (out, err):
        divide(2, 0)
    assert \
        to_string(out) == 'I am going to divide 2 and 0\nWhoops! cannot divide'


def test_printer():
    with captured_output() as (out, err):
        printer("Hello")
    assert to_string(out) == '*' * 30 + '\n' + '%' * 30 + '\nHello\n' \
           + '%' * 30 + '\n' + '*' * 30
