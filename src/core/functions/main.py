# default parameters
def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """
    print("Hello", name + ', ' + msg)


# rest parameters
def greeting(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


# function with return values
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


# recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def lambda_function():
    # double_value = lambda x: x * 2
    def double_value(x): return x * 2

    print(double_value(5))
    # Program to filter out only the even items from a list
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(filter(lambda x: (x % 2 == 0), my_list))
    print(new_list)
    # Program to double each item in a list using map()
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(map(lambda x: x * 2, my_list))
    print(new_list)


def main():
    print(greet('Ray'))
    greet('Ray', 'Welcome!')
    print(greet.__doc__)
    print(absolute_value(2))
    print(absolute_value(-4))
    greeting("Monica", "Luke", "Steve", "John")
    print("The factorial of", 3, "is", factorial(3))
    lambda_function()


if __name__ == '__main__':
    main()
