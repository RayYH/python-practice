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
