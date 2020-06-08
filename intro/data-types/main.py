"""
Data Types
"""

# Integers can be of any length, it is only limited by the memory available.
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1 + 2j
print(a, "is complex number?", isinstance(1 + 2j, complex))

# Lists
# All the items in a list do not need to be of the same type.
simpleList = ["a", 1, 3.14]
print(simpleList)
# slicing operator [ ]
cities = ["Beijing", "Tokyo", "New York", "London", "Paris"]
print(cities)
print(cities[2])
print(cities[0:3])
print(cities[2:])

# Tuple - an ordered sequence of items same as a list.
# Tuples are immutable - which means you cannot use tuple[0]=XXX syntax
myKeywords = ("Ray", "M", 174.8, 24, "Shanghai")
print(myKeywords[0])
print(myKeywords[1:3])

# Strings
# the slicing operator [ ] can be used with strings, and strings are immutable.
s = "This is a string"
print(s)
s = '''A multi-line
string'''
print(s)
print(s[4])
print(s[2:7])

# Sets - an unordered collection of unique items.
simpleSet = {7, 12, "1", True}
# printing set variable
print("a = ", simpleSet)
# data type of variable a
print(type(simpleSet))

# Dictionary - an unordered collection of key-value pairs.
myInfo = {
    "name": "Ray",
    "age": 24
}
print(myInfo)
print(type(myInfo))

# Type casts
print(float(5))
print(float('2.5'))
print(int(10.1))
print(int(-10.1))
print(str(True), type(str(True)))
print(str(2.5), type(str(2.5)))
print(set(simpleList))  # lists to set
print(tuple(simpleSet))  # set to tuple
print(list("string"))  # string to list
print(dict([(3, 26), (4, 44)]))  # array with tuple to dict
