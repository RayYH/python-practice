from src.helper.ioh import captured_output, to_string


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


def producer(cor):
    n = 1
    while n < 100:
        cor.send(n)
        n = n * 2


@coroutine
def my_filter(num, cor):
    while True:
        n = (yield)
        if n < num:
            cor.send(n)


@coroutine
def printer():
    while True:
        n = (yield)
        print(n, sep=" ", end=" ")


def test_printer():
    with captured_output() as (out, err):
        pr = printer()
        fi = my_filter(50, pr)
        producer(fi)
    assert to_string(out) == """1 2 4 8 16 32"""
