"""
operators
see tests/core/operators_test.py
"""


def arithmetic_operators():
    x = 15
    y = 4
    print("x = {}, y = {}".format(x, y))
    # Output: x + y = 19
    print('x + y =', x + y)
    # Output: x - y = 11
    print('x - y =', x - y)
    # Output: x * y = 60
    print('x * y =', x * y)
    # Divide left operand by the right one (always results into float)
    # Output: x / y = 3.75
    print('x / y =', x / y)
    # Floor division - division that results into whole number adjusted to the left in the number line
    # Output: x // y = 3
    print('x // y =', x // y)
    # Output: x % y = 3
    print('x % y =', x % y)
    # Output: x ** y = 50625
    print('x ** y =', x ** y)


def comparison_operators():
    x = 10
    y = 12
    print("x = {}, y = {}".format(x, y))
    # Output: x > y is False
    print('x > y is', x > y)
    # Output: x < y is True
    print('x < y is', x < y)
    # Output: x == y is False
    print('x == y is', x == y)
    # Output: x != y is True
    print('x != y is', x != y)
    # Output: x >= y is False
    print('x >= y is', x >= y)
    # Output: x <= y is True
    print('x <= y is', x <= y)


def logical_operators():
    x = True
    y = False
    print('x and y is', x and y)
    print('x or y is', x or y)
    print('not x is', not x)


def main():
    arithmetic_operators()
    comparison_operators()


if __name__ == '__main__':
    main()
