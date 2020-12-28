from src.helper.ioh import captured_output, to_string
from src.core.io.basic import print_function, output_formatting


def test_print_function():
    with captured_output() as (out, err):
        print_function()
    assert to_string(out) == '''1 2 3 4
1*2*3*4
1#2#3#4&
symbol of zero is 0'''


def test_output_formatting():
    with captured_output() as (out, err):
        output_formatting()
    assert to_string(out) == '''Ray's age is 24
Ray's age is 24
Ray's age is 24
The value of x is 12.35
The value of x is 12.3457'''
