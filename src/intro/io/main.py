"""
Source: https://docs.python.org/3/tutorial/inputoutput.html
Author: Ray

"""

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')
print()

# output formatting
name = "Ray"
age = 24
print('{}\'s age is {}'.format(name, age))
# use tuple index to specify the order
print('{1}\'s age is {0}'.format(age, name))
# or
print('{name}\'s age is {age}'.format(name=name, age=age))

x = 12.3456789
# use % operator
print('The value of x is %3.2f' % x)
print('The value of x is %3.4f' % x)
