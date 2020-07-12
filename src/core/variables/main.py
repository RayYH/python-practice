"""
python variables
"""
# Constants
# In Python, constants are usually declared and assigned in a module.
PI = 3.14
GRAVITY = 9.18
print(PI)
print(GRAVITY)

# Number
my_favorite_number = 0
# String
my_favorite_color = "Blue"
# Assigning multiple values to multiple variables
zero, pi, greet_string = 0, 3.14, "Hello World!"
# Assigning the same value to multiple variables
a = b = c = "abc"
print(my_favorite_number)
print(my_favorite_color)
print(zero, pi, greet_string)
print(a, b, c)

# Number Literals
a = 0b101010  # Binary Literals - with 0b prefix
b = 10000000  # Decimal Literal
c = 0o310136  # Octal Literal - with 0o prefix
d = 0x12ca12  # Hexadecimal Literal - with 0x prefix
e = 10.51234  # Float Literal
f = 1.521e22  # Float Literal
x = 1 + 3.1j  # Complex Literal

# Output: 42 10000000 102494 1231378
print(a, b, c, d)
# Output: 10.51234 1.521e+22
print(e, f)
# Output: (1+3.1j) 1.0 3.1
print(x, x.real, x.imag)

# String literals
strings = "Awesome Python!"
char = "C"
multiline_str = """This is
a multiline string
with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
# Output:
# Awesome Python!
# C
# This is
# a multiline string
# with more than one line code.
# Ünicöde
# raw \n string

# Boolean literals
# In Python, True represents the value as 1 and False as 0.
a = True + 4
b = False + 10
print("a:", a)  # 5
print("b:", b)  # 10

# Python contains one special literal i.e. None. We use it
# to specify that the field has not been created.
drink = "Available"
food = None


def _menu(arg):
    if arg == drink:
        print(drink)
        print(type(drink))  # <class 'str'>
    else:
        print(food)
        print(type(food))  # <class 'NoneType'>


_menu(drink)
_menu("not exists")
# Output
# Available
# <class 'str'>
# None
# <class 'NoneType'>

# Literal collections
fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
# Output
# ['apple', 'mango', 'orange']
# (1, 2, 3)
# {'a': 'apple', 'b': 'ball', 'c': 'cat'}
# {'a', 'i', 'o', 'u', 'e'}
