NUM = 60


def star(func):

    def inner(*args, **kwargs):
        print_symbol("*")
        func(*args, **kwargs)
        print_symbol("*")

    return inner


def dash(func):

    def inner(*args, **kwargs):
        print_symbol("-")
        func(*args, **kwargs)
        print_symbol("-")

    return inner


def print_symbol(symbol):
    print(symbol[0] * NUM)
