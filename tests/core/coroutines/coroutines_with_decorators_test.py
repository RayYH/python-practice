from src.helper.ioh import captured_output, to_string


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


@coroutine
def bare_bones():
    while True:
        value = (yield)
        print(value)


def test_bare_bones():
    with captured_output() as (out, err):
        # no longer need to use the next() method
        cor = bare_bones()
        cor.send("Using a decorator!")
    assert to_string(out) == "Using a decorator!"
