from src.c.add import add_int, add_float
from src.helper.sysh import is_darwin


def test_add_int():
    if is_darwin():
        assert add_int(4, 5) == 9
        assert add_int(1, 2) == 3


def test_add_float():
    if is_darwin():
        assert round(add_float(4.1, 5.5), 2) == 9.60
