import pytest


class Person:
    """A simple Person class"""
    age = 10

    def get_age(self):
        return self.age


def test_person_class_attributes():
    # MyClass.i and MyClass.f are valid attribute references
    assert Person.age == 10
    # class methods output as strings
    assert '{}'.format(Person.get_age).startswith("<function Person.get_age")
    # get class docstring
    assert Person.__doc__ == "A simple Person class"


def test_create_an_object_of_person_class():
    ray = Person()
    ray.age = 25
    assert ray.age == 25
    assert ray.get_age() == 25
    assert '{}'.format(ray.get_age).startswith("<bound method Person.get_age")


class ComplexNumber:
    # class instantiation automatically invokes __init__()
    # for the newly-created class instance.
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    # @staticmethod annotation indicates static method
    @staticmethod
    def init_complex_number(r, i):
        return ComplexNumber(r=r, i=i)

    # normal instance method
    def to_string(self):
        return '{} + {}j'.format(self.real, self.imag)


def test_complex_number_initialization():
    # create a new ComplexNumber object by passing two parameters
    cn_1 = ComplexNumber(2, 3)
    assert cn_1.real == 2
    assert cn_1.imag == 3
    # only passing one parameter
    cn_2 = ComplexNumber(5)
    assert cn_2.real == 5
    assert cn_2.imag == 0
    # via static method
    cn_3 = ComplexNumber.init_complex_number(1, 2)
    assert cn_3.real == 1
    assert cn_3.imag == 2


def test_dynamically_add_attrs():
    cn = ComplexNumber(1, 2)
    cn.counter = 1
    while cn.counter < 10:
        cn.counter = cn.counter * 2
    assert cn.counter == 16
    del cn.counter
    with pytest.raises(AttributeError):
        assert not cn.counter


def test_complex_number_instance_methods():
    cn = ComplexNumber(2, 3)
    assert cn.to_string() == "2 + 3j"
