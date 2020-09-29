from src.core.oop.inheritance import Penguin
from src.helper.io import captured_output, to_string


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


def test_multiple_inheritance():
    # Method Resolution Order (MRO)
    assert '{}'.format(M.mro()).replace("class ", "").replace(
        "inheritance_test.",
        "") == "[<'M'>, <'B'>, <'A'>, <'X'>, <'Y'>, <'Z'>, <'object'>]"


def test_penguin():
    with captured_output() as (out, err):
        peggy = Penguin()
        # Bird is ready
        # Penguin is ready
        peggy.who_is_this()
        # Penguin
        # Penguin
        peggy.swim()
        # Bird
        # Penguin swim faster
        peggy.run()
        # Penguin
        # Penguin run faster
    assert to_string(out) == '''Bird is ready
Penguin is ready
Penguin
Penguin
Bird
Penguin swim faster
Penguin
Penguin run faster'''
