# default parameters
def get_greeting_string(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """
    return "Hello " + name + ', ' + msg


def test_get_greeting_string():
    assert get_greeting_string("Ray") == "Hello Ray, Good morning!"
    assert get_greeting_string("Ray", "Welcome!") == "Hello Ray, Welcome!"


# rest parameters
def get_greeting_strings(*names):
    """
    This function greets all
    the person in the names tuple.
    """
    my_list = []
    # names is a tuple with arguments
    for name in names:
        my_list.append("Hello " + name)
    return my_list


def test_get_greeting_strings():
    my_lists = get_greeting_strings("Monica", "Luke", "Steve", "John")
    assert my_lists == [
        "Hello Monica",
        "Hello Luke",
        "Hello Steve",
        "Hello John"
    ]
    assert get_greeting_strings.__doc__ == '''
    This function greets all
    the person in the names tuple.
    '''


# function with return values
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


def test_absolute_value():
    assert absolute_value(2) == 2
    assert absolute_value(-4) == 4


# recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def test_factorial():
    assert factorial(3) == 6
    assert factorial(4) == 24


def test_lambda_function():
    # double_value = lambda x: x * 2
    def double_value(x): return x * 2

    assert double_value(5) == 10
    # Program to filter out only the even items from a list
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(filter(lambda x: (x % 2 == 0), my_list))
    assert new_list == [4, 6, 8, 12]
    # Program to double each item in a list using map()
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(map(lambda x: x * 2, my_list))
    assert new_list == [2, 10, 8, 12, 16, 22, 6, 24]
