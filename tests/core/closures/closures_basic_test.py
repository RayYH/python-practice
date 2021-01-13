"""
Python functions are first-class citizens. This means that functions have equal
status with other objects in Python. Functions can be assigned to variables,
stored in collections, created and deleted dynamically, or passed as arguments.
"""


def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


def test_functions_can_be_assigned_to_variables():
    times3 = make_multiplier_of(3)
    times5 = make_multiplier_of(5)
    assert times3(9) == 27
    assert times5(9) == 45
