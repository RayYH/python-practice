PI = 3.14
GRAVITY = 9.18


def test_constants():
    assert PI == 3.14
    assert GRAVITY == 9.18


def test_variables_basic():
    my_favorite_number = 0
    # String
    my_favorite_color = "Blue"
    # Assigning multiple values to multiple variables
    zero, pi, greet_string = 0, 3.14, "Hello World!"
    # Assigning the same value to multiple variables
    a = b = c = "abc"
    assert my_favorite_number == 0
    assert my_favorite_color == "Blue"
    assert zero == 0
    assert pi == 3.14
    assert greet_string == "Hello World!"
    assert a == "abc"
    assert b == "abc"
    assert c == "abc"


def test_number_literals():
    a = 0b101010  # Binary Literals - with 0b prefix
    b = 10000000  # Decimal Literal
    c = 0o310136  # Octal Literal - with 0o prefix
    d = 0x12ca12  # Hexadecimal Literal - with 0x prefix
    e = 10.51234  # Float Literal
    f = 1.521e22  # Float Literal
    x = 1 + 3.1j  # Complex Literal
    assert a == 42
    assert b == 10000000
    assert c == 102494
    assert d == 1231378
    assert e == 10.51234
    assert f == 1.521e+22
    assert x == 1 + 3.1j
    assert x.real == 1
    assert x.imag == 3.1


def test_string_literals():
    # String literals
    strings = "Awesome Python!"
    char = "C"
    multiline_str = """This is
    a multiline string
    with more than one line code."""
    unicode = u"\u00dcnic\u00f6de"
    raw_str = r"raw \n string"
    assert strings == "Awesome Python!"
    assert char == "C"
    assert multiline_str == '''This is
    a multiline string
    with more than one line code.'''
    assert unicode == 'Ünicöde'
    assert raw_str == 'raw \\n string'


def test_boolean_literals():
    a = True + 4
    b = False + 10
    assert a == 5
    assert b == 10


def _menu(arg):
    drink = "Available"
    food = None
    if arg == drink:
        return '{} {}'.format(drink, type(drink))
    else:
        return '{} {}'.format(food, type(food))


def test_none_type():
    assert _menu("Available") == "Available <class 'str'>"
    assert _menu("not exists") == "None <class 'NoneType'>"


def test_collection_literals():
    fruits = ["apple", "mango", "orange"]  # list
    numbers = (1, 2, 3)  # tuple
    alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
    vowels = {'a', 'e', 'i', 'o', 'u'}  # set
    assert '{}'.format(fruits) == "['apple', 'mango', 'orange']"
    assert '{}'.format(numbers) == "(1, 2, 3)"
    assert '{}'.format(alphabets) == "{'a': 'apple', 'b': 'ball', 'c': 'cat'}"
    assert len(vowels) == 5  # order is not certain
