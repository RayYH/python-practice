# Demonstration of MRO

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
    # Method Resolution Order (MRO).
    assert '{}'.format(M.mro()).replace("class ", "").replace("inheritance_test.", "") \
           == "[<'M'>, <'B'>, <'A'>, <'X'>, <'Y'>, <'Z'>, <'object'>]"
