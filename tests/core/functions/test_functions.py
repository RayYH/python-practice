from src.helper.ioh import captured_output, to_string


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
        "Hello Monica", "Hello Luke", "Hello Steve", "Hello John"
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
    def double_value(x):
        return x * 2

    assert double_value(5) == 10
    # Program to filter out only the even items from a list
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(filter(lambda x: (x % 2 == 0), my_list))
    assert new_list == [4, 6, 8, 12]
    # Program to double each item in a list using map()
    my_list = [1, 5, 4, 6, 8, 11, 3, 12]
    new_list = list(map(lambda x: x * 2, my_list))
    assert new_list == [2, 10, 8, 12, 16, 22, 6, 24]


# *args is used to send a non-keyworded variable length argument list
def var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


def test_var_args():
    with captured_output() as (out, err):
        var_args('apple', 'orange', 'banana', 'peach')
    assert to_string(out) == '''first normal arg: apple
another arg through *argv: orange
another arg through *argv: banana
another arg through *argv: peach'''


# **kwargs allows you to pass keyworded variable length of arguments
# to a function.
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


def test_greet_me():
    with captured_output() as (out, err):
        greet_me(name="Ray")
    assert to_string(out) == "name = Ray"


def args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


def test_args_kwargs():
    args = ("two", 3, 5)
    with captured_output() as (out, err):
        args_kwargs(*args)
    assert to_string(out) == '''arg1: two
arg2: 3
arg3: 5'''
    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    with captured_output() as (out, err):
        args_kwargs(**kwargs)
    assert to_string(out) == '''arg1: 5
arg2: two
arg3: 3'''


def user_info(**kwargs):
    if 'name' in kwargs:
        return kwargs['name']
    elif 'age' in kwargs:
        return kwargs['age']
    else:
        return None


def test_user_info():
    assert not user_info()
    assert user_info(age=24) == 24
    assert user_info(name='Ray', age=24) == 'Ray'
