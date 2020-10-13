from functools import wraps


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


# The order in which we chain decorators matter.
@star
@percent
def printer(msg):
    print(msg)


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrap_the_function():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrap_the_function


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")
