def test_arithmetic_operators():
    x = 15
    y = 4
    assert x + y == 19
    assert x - y == 11
    assert x * y == 60
    # division always returns a floating point number
    assert x / y == 3.75
    # floor division discards the fractional part
    assert x // y == 3
    # the % operator returns the remainder of the division
    assert x % y == 3
    # y to the power pf x
    assert x ** y == 50625


def test_comparison_operators():
    x = 10
    y = 12
    assert not x > y
    assert x < y
    assert not x == y
    assert x != y
    assert not x >= y
    assert x <= y


def test_logical_operators():
    x = True
    y = False
    assert not (x and y)
    assert x or y
    assert not y
    assert y is not True


def test_bitwise_operators():
    # 5 = 0000 0101
    a = 5
    # 9 = 0000 1001
    b = 9
    # And
    # 5 & 9
    # 5 = 0000 0101
    # 9 = 0000 1001
    # -------------
    #   = 0000 0001
    #   = 1
    assert a & b == 1
    # Or
    #  5 | 9
    # 5 = 0000 0101
    # 9 = 0000 1001
    # -------------
    #   = 0000 1101
    #   = 1 + 4 + 8
    assert a | b == 1 + 4 + 8
    # Xor
    # 5 ^ 9
    # 5 = 0000 0101
    # 9 = 0000 1001
    # -------------
    #   = 0000 1100
    #   = 4 + 8
    assert a ^ b == 4 + 8
    # Complement
    # 4
    # 0000 0100 - true code -> below is an inverse form
    # 1111 1011 - will be treated as a 2's complement,
    #           - this is a negative number
    #           - so, to get the true code, minus one first
    # 1111 1010 - then, inverse all numbers except the sign
    # 1000 0101
    #
    # There is a simple rule: A + (~A) = -1
    assert ~4 == -(1 + 4)
    # bit shift operators
    assert 212 >> 0 == 212
    assert 212 >> 1 == 212 // 2
    assert 212 >> 2 == 212 // 4
    assert 212 >> 3 == 212 // 8
    assert 212 << 0 == 212
    assert 212 << 1 == 424
    assert 212 << 2 == 848
    assert 212 << 3 == 1696


def test_assignment_operators():
    a = 5
    b = 5
    assert a == b
    a += 5
    b = b + 5
    assert a == b
    a -= 5
    b = b - 5
    assert a == b
    a *= 5
    b = b * 5
    assert a == b
    a /= 5
    b = b / 5
    assert a == b
    a %= 5
    b = b % 5
    assert a == b
    a //= 5
    b = b // 5
    assert a == b
    a **= 5
    b = b ** 5
    assert a == b
    a = 5
    b = 5
    a &= 5
    b = b & 5
    assert a == b
    a |= 5
    b = b | 5
    assert a == b
    a ^= 5
    b = b ^ 5
    assert a == b
    a >>= 5
    b = b >> 5
    assert a == b
    a <<= 5
    b = b << 5
    assert a == b


def test_identity_operators():
    x1 = 5
    y1 = 5
    x2 = 'Hello'
    y2 = 'Hello'
    x3 = [1, 2, 3]
    y3 = [1, 2, 3]
    assert (x1 is y1)
    assert (x2 is y2)
    # x3 and y3 are lists. They are equal but not identical.
    # It is because the interpreter locates them separately in memory
    # although they are equal.
    assert (x3 is not y3)


def test_membership_operators():
    # in - True if value/variable is found in the sequence
    # In a dictionary we can only test for presence of key, not the value.
    # we can test whether a value or variable is found in a sequence
    # (string, list, tuple, set and dictionary).
    x = 'Hello world'
    y = {1: 'a', 2: 'b'}
    assert ('H' in x)
    assert ('hello' not in x)
    assert (1 in y)
    assert ('a' not in y)


def test_ternary_operator():
    # Ternary operators are more commonly known as conditional
    # expressions in Python.
    # value_if_true if condition else value_if_false
    is_nice = True
    state = "nice" if is_nice else "not nice"
    assert state == 'nice'
    # (if_test_is_false, if_test_is_true)[test]
    nice = True
    personality = ("mean", "nice")[nice]
    assert personality == 'nice'
    # ShortHand Ternary
    assert True or "Some"
    assert (False or "Some") == "Some"
