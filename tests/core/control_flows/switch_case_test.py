"""
Python does not support switch-case statement,
but we can use a function to make it.
"""


def switched(option, choices):
    # in case option does dot exists
    # we use get() instead of [] syntax
    return choices.get(option)


def switched_with_defaults(option, choices, default):
    return choices.get(option, default)


def test_switch_case():
    choices = {"a": 1, "b": 2, "c": 3}
    assert switched("a", choices) == 1
    assert switched("b", choices) == 2
    assert switched("c", choices) == 3
    assert not switched("d", choices)
    assert switched_with_defaults("d", choices, 4) == 4
