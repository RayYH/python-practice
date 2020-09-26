"""
1. Integers can be of any length, it is only limited by the memory available.
2. A floating-point number is accurate up to 15 decimal places.
3. We can use the type() function to know which class a variable or a value belongs to.
4. The isinstance() function is used to check if an object belongs to a particular class.
"""
from decimal import Decimal
from fractions import Fraction
import fractions
import math
import random


def test_check_numbers_type():
    # use type to check variable's types
    assert '{}'.format(type(1)) == "<class 'int'>"
    assert '{}'.format(type(1.0)) == "<class 'float'>"
    # use isinstance to check if given object is an instance of a class
    assert isinstance(1 + 2j, complex)


def test_float_point_numbers_got_truncated():
    # got truncated
    assert '{}'.format(0.1234567890123456789) == '0.12345678901234568'


def test_radix_and_its_conversions():
    # radix
    assert 0b1101011 == 107
    assert 0xFB + 0b10 == 253
    assert 0o15 == 13
    assert '{}'.format(int(0b1101011)) == '107'
    assert '{}'.format(bin(107)) == '0b1101011'
    assert '{}'.format(hex(107)) == '0x6b'
    assert '{}'.format(oct(107)) == '0o153'


def test_operations_between_int_and_floating_numbers():
    # operations between int and float values
    assert 1 + 2.0 == 3.0
    assert int(2.3) == 2
    assert int(-2.8) == -2
    assert float(5) == 5.0
    assert complex('3+5j') == (3 + 5j)
    assert (1.1 + 2.2) != 3.3
    assert 2 + 2 == 4
    assert 50 - 5 * 6 == 20
    assert (50 - 5 * 6) / 4 == 5.0
    assert 4 * 3.75 - 1 == 14.0
    assert 8 / 5 == 1.6  # division always returns a floating point number
    assert 17 / 3 == 5.666666666666667  # classic division returns a float
    assert 17 // 3 == 5  # floor division discards the fractional part
    assert 17 % 3 == 2  # the % operator returns the remainder of the division
    assert 5 * 3 + 2 == 17  # result * divisor + remainder
    assert 5 ** 2 == 25  # 5 squared
    assert 2 ** 7 == 128  # 2 to the power of 7
    width = 20
    height = 5 * 9
    assert width * height == 900
    tax = 12.5 / 100
    price = 100.50
    assert price * tax == 12.5625
    # In interactive mode, the last printed expression is assigned to the variable _
    assert round(price + price * tax, 2) == 113.06


def test_decimal_module():
    assert Decimal('1.1') + Decimal('2.2') == Decimal('3.3')
    assert Decimal('1.2') * Decimal('2.50') == Decimal('3.000')


def test_fraction_module():
    assert fractions.Fraction(1.5) == 3 / 2
    assert fractions.Fraction(5) == 5
    assert fractions.Fraction(1, 3) != 1 / 3
    assert fractions.Fraction(1.1) == 2476979795053773 / 2251799813685248
    assert (Fraction(-3, 10) < 0)


def test_math_module():
    assert math.pi == 3.141592653589793
    assert math.cos(math.pi) == -1.0
    assert math.exp(10) == 22026.465794806718
    assert math.log10(1000) == 3.0
    assert math.sinh(1) == 1.1752011936438014
    assert math.factorial(6) == 720


def test_random_module():
    assert random.randrange(10, 20) in range(10, 20)
    x = ['a', 'b', 'c', 'd', 'e']
    # Get random choice
    assert random.choice(x) in x
    assert random.random() >= 0
    assert random.random() <= 1
