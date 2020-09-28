"""
Python does not support switch-case statement,
but we can use a function to make it.
"""


def switched(option, choices):
    return choices.get(option)  # in case option does dot exists


def switched_with_defaults(option, choices, default):
    return choices.get(option, default)
