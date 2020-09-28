def print_function():
    print(1, 2, 3, 4)
    # 1 2 3 4
    print(1, 2, 3, 4, sep='*')
    # 1*2*3*4
    print(1, 2, 3, 4, sep='#', end='&')
    print()
    # 1#2#3#4&
    print("symbol of zero is", 0)
    # zero symbol is 0


def output_formatting():
    """
    We can use str.format() func to format a string
    see tests/core/format/formatting_test.py
    """
    name = "Ray"
    age = 24
    print('{}\'s age is {}'.format(name, age))
    # We can use tuple index to specify the order
    print('{1}\'s age is {0}'.format(age, name))
    print('{name}\'s age is {age}'.format(name=name, age=age))
    # Ray's age is 24

    x = 12.3456789
    # use % operator
    print('The value of x is %3.2f' % x)
    print('The value of x is %3.4f' % x)
    # The value of x is 12.35
    # The value of x is 12.3457


def main():
    print_function()
    output_formatting()


if __name__ == '__main__':
    main()
