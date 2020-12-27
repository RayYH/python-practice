import pytest


def test_create_a_string():
    # single quotes
    first_string = 'str'
    # double quotes
    second_string = "str"
    # triple quotes
    third_string = '''str'''
    fourth_string = """str"""
    assert first_string == second_string == third_string == fourth_string


def test_raw_string():
    # here \n means newline!
    assert '\name' == """
ame"""
    # use raw strings by adding an r before the first quote
    assert r'\name' == '\\name'


def test_unicode_points():
    assert '\u4E2D\u6587' == '中文'


def test_multiple_line_strings():
    # triple quotes string can extend multiple lines
    my_string = """Hello, welcome to
    the world of Python"""
    assert my_string.startswith("H")
    # end of lines are automatically included in the string
    my_string = """
    Hello, welcome to
    the world of Python"""
    assert my_string.startswith("\n")
    # it’s possible to prevent this by adding a \ at the end of the line
    my_string = """\
Hello, welcome to\
 the world of Python"""
    assert my_string == "Hello, welcome to the world of Python"


def test_access_characters_in_string():
    """
    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6  -5  -4  -3  -2  -1
    """
    word = 'Python'
    # character in position 0
    assert word[0] == 'P'
    # character in position 5
    assert word[5] == 'n'
    # last character
    assert word[-1] == 'n'
    # second-last character
    assert word[-2] == 'o'
    # characters from position 0 (included) to 2 (excluded)
    assert word[0:2] == 'Py'
    # characters from position 2 (included) to 5 (excluded)
    assert word[2:5] == 'tho'
    # s[:i] + s[i:] is always equal to s
    assert word[:2] + word[2:] == word
    assert word[:4] + word[4:] == word
    # character from the beginning to position 2 (excluded)
    assert word[:2] == 'Py'
    # characters from position 4 (included) to the end
    assert word[4:] == 'on'
    # characters from the second-last (included) to the end
    assert word[-2:] == 'on'
    # Attempting to use an index that is too large will result in an error
    with pytest.raises(IndexError):
        assert word[42]
    # out of range slice indexes are handled gracefully when used for slicing
    assert word[4:42] == 'on'
    assert word[42:] == ''


def test_string_is_immutable():
    word = 'Python'
    with pytest.raises(TypeError):
        word[0] = 'A'
    with pytest.raises(TypeError):
        word[2:] = 'py'


def test_string_operations():
    str1 = 'Py'
    str2 = 'thon'
    # concatenated with the + operator
    assert str1 + str2 == 'Python'
    # repeated with the * operator
    assert str1 * 3 == 'PyPyPy'
    # Two or more string literals (only literals, can't be variables) next to
    # each other are automatically concatenated
    assert 'Py' 'thon' == 'Python'
    # This feature is particularly useful when you want to break long strings
    text = ('Put several strings within parentheses '
            'to have them joined together.')
    assert text == """Put several strings within\
 parentheses to have them joined together."""


def test_iterating_through_a_string():
    # Iterating through a string
    count = 0
    for letter in 'Hello World':
        if letter == 'l':
            count += 1
    assert count == 3


def test_string_membership():
    assert 'a' in 'program'
    assert 'at1' not in 'battle'


def test_string_functions():
    s = 'supercalifragilisticexpialidocious'
    # len() returns the length of a string:
    assert len(s) == 34
    my_str = 'cold'
    # cast string to list
    list_enumerate = list(enumerate(my_str))
    assert list_enumerate == [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
    my_str = 'Hello, world!'
    assert my_str.title() == "Hello, World!"
    assert my_str.upper() == "HELLO, WORLD!"
    assert my_str.lower() == "hello, world!"
    assert not my_str.isupper()
    assert my_str.startswith("Hello")
    assert not my_str.endswith("World")
