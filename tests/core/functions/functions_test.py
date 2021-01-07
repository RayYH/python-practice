from src.helper.ioh import captured_output, to_string


def test_default_parameters():
    def get_greeting_string(name, msg="Good morning!"):
        return "Hello " + name + ', ' + msg

    assert get_greeting_string("Ray") == "Hello Ray, Good morning!"
    assert get_greeting_string("Ray", "Welcome!") == "Hello Ray, Welcome!"


def test_positional_arguments():
    def get_greeting_strings(*names):
        my_list = []
        for name in names:
            my_list.append("Hello " + name)
        return my_list

    my_lists = get_greeting_strings("Monica", "Luke", "Steve", "John")
    assert my_lists == [
        "Hello Monica", "Hello Luke", "Hello Steve", "Hello John"
    ]


def test_recursive_function():
    def factorial(x):
        if x == 1:
            return 1
        else:
            return x * factorial(x - 1)

    assert factorial(3) == 6
    assert factorial(4) == 24


def test_lambda_functions():
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


def test_positional_arguments_as_a_tuple():
    def var_args(formal_arg, *argv):
        print("first normal arg:", formal_arg)
        for arg in argv:
            print("another arg through *argv:", arg)

    with captured_output() as (out, err):
        var_args('apple', 'orange', 'banana', 'peach')
    assert to_string(out) == '''first normal arg: apple
another arg through *argv: orange
another arg through *argv: banana
another arg through *argv: peach'''


def test_keyword_arguments_as_a_dict():
    def greet_me(**kwargs):
        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))

    with captured_output() as (out, err):
        greet_me(name="Ray")
    assert to_string(out) == "name = Ray"


def test_named_arguments():
    def args_kwargs(arg1, arg2, arg3):
        print("arg1:", arg1)
        print("arg2:", arg2)
        print("arg3:", arg3)

    # positional arguments
    args = ("two", 3, 5)
    with captured_output() as (out, err):
        args_kwargs(*args)
    assert to_string(out) == '''arg1: two
arg2: 3
arg3: 5'''

    # keyword arguments
    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    with captured_output() as (out, err):
        args_kwargs(**kwargs)
    assert to_string(out) == '''arg1: 5
arg2: two
arg3: 3'''


def test_arbitrary_arguments():
    def concat(*args, sep='/'):
        return sep.join(args)

    assert concat("earth", "mars", "venus") == 'earth/mars/venus'
    assert concat("earth", "mars", "venus", sep=".") == 'earth.mars.venus'


def test_unpacking_argument_lists():
    # normal call with separate arguments
    assert list(range(3, 6)) == [3, 4, 5]
    # call with arguments unpacked from a list
    assert list(range(*[3, 6])) == [3, 4, 5]

    def user(name, language='Chinese', number=1):
        return '{} speaks {}, his favorite number is {}'.format(
            name, language, number)

    u = {'name': 'Ray', 'language': 'English', "number": 0}
    assert user(**u) == "Ray speaks English, his favorite number is 0"
