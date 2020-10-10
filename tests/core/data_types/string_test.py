"""
1. String is sequence of Unicode characters.
2. We can use single quotes or double quotes to represent strings.
3. Multi-line strings can be denoted using triple quotes, three of ' or ".
4. The slicing operator [ ] can be used with strings.
5. Strings are immutable - we cannot use an assignment statement like str[5]
   = 'A'.
"""


def test_create_a_string():
    first_string = 'Hello'
    assert first_string == first_string
    second_string = "Hello"
    assert first_string == second_string
    second_string = '''Hello'''
    assert first_string == second_string
    # triple quotes string can extend multiple lines
    my_string = """Hello, welcome to
               the world of Python"""
    assert my_string
    # raw string
    assert r'C:\Users\Ray\Documents' == 'C:\\Users\\Ray\\Documents'
    # unicode
    my_str = '\u4E2D\u6587'
    assert my_str == '中文'


def test_access_characters_in_string():
    my_str = 'some word'
    assert my_str == my_str
    assert my_str[0] == 's'
    assert my_str[-1] == 'd'
    assert my_str[1:5] == "ome "
    assert my_str[5:-2] == "wo"
    # Strings are immutable.


def test_string_operations():
    str1 = 'Hello'
    str2 = 'World!'
    assert str1 + ' ' + str2 == 'Hello World!'
    assert str1 * 3 == 'HelloHelloHello'
    assert 'Hello ' 'World!' == 'Hello World!'
    s = 'Hello ' 'World!'
    assert s == 'Hello World!'


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
    my_str = 'cold'
    list_enumerate = list(enumerate(my_str))
    assert list_enumerate == [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
    assert len(my_str) == 4
    my_str = 'Hello, world!'
    assert len(my_str) == 13
    assert my_str.title() == "Hello, World!"
    assert my_str.upper() == "HELLO, WORLD!"
    assert my_str.lower() == "hello, world!"
    assert not my_str.isupper()
    assert my_str.startswith("Hello")
    assert not my_str.endswith("World")
