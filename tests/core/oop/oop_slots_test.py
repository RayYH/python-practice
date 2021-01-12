"""
In Python every class can have instance attributes. By default Python uses a
dict to store an object’s instance attributes. This is really helpful as it
allows setting arbitrary new attributes at runtime.

However, for small classes with known attributes it might be a bottleneck. The
dict wastes a lot of RAM. Python can’t just allocate a static amount of memory
at object creation to store all the attributes.

__slots__ tells Python not to use a dict, and only allocate space for a fixed
set of attributes.
"""
import pytest


class MyClassWithoutSlots(object):
    def __init__(self):
        self.name = "Ray"
        self.age = 24


class MyClassWithSlots(object):
    __slots__ = ['name', 'age']

    def __init__(self):
        self.name = "Ray"
        self.age = 24


def test_class_without_slots():
    my_class_without_slots = MyClassWithoutSlots()
    assert my_class_without_slots.__dict__['name'] == 'Ray'
    assert my_class_without_slots.__dict__['age'] == 24


def test_class_with_slots():
    my_class_with_slots = MyClassWithSlots()
    assert my_class_with_slots.name == "Ray"
    assert my_class_with_slots.age == 24
    my_class_with_slots.name = "Tom"
    assert my_class_with_slots.name == "Tom"
    with pytest.raises(AttributeError):
        print(my_class_with_slots.__dict__)
