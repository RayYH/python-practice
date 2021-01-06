import math
from src.helper.ioh import captured_output, to_string


def test_float_rounds():
    assert f'{math.pi:.3f}' == '3.142'


def test_characters_wide():
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    with captured_output() as (out, err):
        for name, phone in table.items():
            print(f'{name:10} ==> {phone:10d}')
    assert to_string(out) == """\
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678\
"""
