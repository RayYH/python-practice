"""
Data Types
Author: ray
Link: https://www.programiz.com/python-programming/variables-datatypes
"""


def python_numbers():
    """
    Integers can be of any length, it is only limited by the memory available.
    A floating-point number is accurate up to 15 decimal places.
    we can use the type() function to know which class a variable or a value belongs to.
    the isinstance() function is used to check if an object belongs to a particular class.
    """
    a = 5
    print(a, "is of type", type(a))
    # 5 is of type <class 'int'>

    a = 2.0
    print(a, "is of type", type(a))
    # 2.0 is of type <class 'float'>

    a = 1 + 2j
    print(a, "is complex number?", isinstance(1 + 2j, complex))
    # (1+2j) is complex number? True

    b = 0.1234567890123456789
    print(b)
    # 0.12345678901234568 - got truncated


def python_lists():
    """
    List is an ordered sequence of items.
    All the items in a list do not need to be of the same type.
    We can use the slicing operator [ ] to extract an item or a range of items from a list.
    """
    simple_list = ["a", 1, 3.14, 1]
    print(simple_list)
    # ['a', 1, 3.14, 1]
    cities = ["Beijing", "Tokyo", "New York", "London", "Paris"]
    print(cities)
    # ['Beijing', 'Tokyo', 'New York', 'London', 'Paris']
    print(cities[2])
    # New York
    print(cities[0:3])
    # ['Beijing', 'Tokyo', 'New York']
    print(cities[2:])
    # ['New York', 'London', 'Paris']
    print(set(simple_list))  # lists to set
    # {1, 3.14, 'a'}


def python_tuples():
    """
    Tuple is an ordered sequence of items same as a list.
    Tuples are immutable - which means you cannot use an assignment statement like tuple[0]=XX.
    """
    my_keywords = ("Ray", "M", 174.8, 24, "Shanghai")
    print(my_keywords)
    # ('Ray', 'M', 174.8, 24, 'Shanghai')
    print(my_keywords[0])
    # Ray
    print(my_keywords[1:3])
    # ('M', 174.8)


def python_strings():
    """
    String is sequence of Unicode characters.
    We can use single quotes or double quotes to represent strings.
    Multi-line strings can be denoted using triple quotes, three of ' or ".
    The slicing operator [ ] can be used with strings, and strings are immutable.
    Strings are immutable - we cannot use an assignment statement like str[5] = 'A'.
    """
    s = "This is a string"
    print(s)
    # This is a string
    s = '''A multi-line
    string'''
    print(s)
    # A multi-line
    #     string
    print(s[4])
    # l
    print(s[2:7])
    # multi


def python_sets():
    """
    Set is an unordered collection of unique items.
    Items in a set are not ordered, indexing has no meaning.
    """
    simple_set = {7, 12, "1", True}
    print(simple_set)
    # {True, '1', 12, 7}
    print(type(simple_set))
    # <class 'set'>
    print(tuple(simple_set))
    # (True, '1', 12, 7)
    a = {1, 2, 2, 3, 3, 3}  # intersection
    print(a)
    # {1, 2, 3}


def python_dictionaries():
    """
    Dictionary is an unordered collection of key-value pairs.
    Dictionaries are optimized for retrieving data, but we must know the key to retrieve the value.
    Key and value can be of any type.
    """
    my_info = {
        "name": "Ray",
        "age": 24
    }
    print(my_info)
    # {'name': 'Ray', 'age': 24}
    print(type(my_info))
    # <class 'dict'>


def type_conversions():
    """
    We can convert between different data types by using different type conversion functions like int(), float(), str()
    Conversion from float to int will truncate the value (make it closer to zero).
    Conversion to and from string must contain compatible values.
    To convert to dictionary, each element must be a pair:
    """
    print(int(10.1))
    # 10
    print(int(-10.1))
    # -10
    print(float(5))
    # 5.0
    print(float('2.5'))
    # 2.5
    print(str(True), type(str(True)))
    # True <class 'str'>
    print(str(2.5), type(str(2.5)))
    # 2.5 <class 'str'>
    print(list("string"))
    # ['s', 't', 'r', 'i', 'n', 'g']
    print(dict([(3, 26), (4, 44)]))
    # {3: 26, 4: 44}
    num_int = 123
    num_flo = 1.23
    num_new = num_int + num_flo
    print(type(num_new))
    # <class 'float'>


def main():
    python_numbers()
    python_lists()
    python_tuples()
    python_strings()
    python_sets()
    python_dictionaries()
    type_conversions()


if __name__ == '__main__':
    main()
