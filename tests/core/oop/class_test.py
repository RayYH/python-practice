class Person:
    """This is a person class"""
    age = 10

    def get_age(self):
        return self.age


class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    @staticmethod
    def init_complex_number(r, i):
        return ComplexNumber(r=r, i=i)

    def get_data(self):
        return '{} + {}j'.format(self.real, self.imag)


def test_person():
    assert Person.age == 10
    assert '{}'.format(
        Person.get_age).startswith("<function Person.get_age at")
    assert Person.__doc__ == "This is a person class"
    harry = Person()
    assert harry.age == 10
    # harry.get_age() translates into Person.get_age(harry)
    assert harry.get_age() == 10
    assert '{}'.format(
        harry.get_age).startswith("<bound method Person.get_age of")


def test_complex_number():
    # Create a new ComplexNumber object
    num1 = ComplexNumber(2, 3)
    # Call get_data() method
    assert num1.get_data() == "2 + 3j"
    # Create another ComplexNumber object
    # and create a new attribute 'attr'
    num2 = ComplexNumber(5)
    num2.attr = 10
    assert num2.real == 5
    assert num2.imag == 0
    assert num2.attr == 10
    # we can use del syntax to delete attributes & methods
    del num2.attr
    # removes the binding between num2 & ComplexNumber class
    del num2
    c = ComplexNumber.init_complex_number(1, 2)
    assert c.real == 1
    assert c.imag == 2
