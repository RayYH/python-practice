"""
In the most basic sense, a decorator is a callable that returns a callable.
"""
from src.core.decorators.celsius import *


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


def test_operate():
    assert operate(inc, 3) == 4
    assert operate(dec, 3) == 2


def test_celsius():
    human = Celsius()
    human.temperature = 37
    assert human.temperature == 37
    assert human.to_fahrenheit() == 98.60000000000001
    assert human.__dict__ == {'temperature': 37}


def test_celsius_with_getters_and_setters():
    human = CelsiusWithGetterAndSetters(37)
    assert human.get_temperature() == 37
    assert human.to_fahrenheit() == 98.60000000000001
    human.set_temperature(-1)
    assert human.to_fahrenheit() == 30.2
    assert human.__dict__ == {'_temperature': -1}


def test_celsius_with_property_class():
    human = CelsiusWithPropertyClass(37)
    assert human.get_temperature() == 37
    assert human.to_fahrenheit() == 98.60000000000001
    human.temperature = -1
    assert human.to_fahrenheit() == 30.2
    assert human.__dict__ == {'_temperature': -1}


def test_celsius_with_property_decorator():
    human = CelsiusWithPropertyClass(37)
    assert human.get_temperature() == 37
    assert human.to_fahrenheit() == 98.60000000000001
    human.temperature = -1
    assert human.to_fahrenheit() == 30.2
    assert human.__dict__ == {'_temperature': -1}
