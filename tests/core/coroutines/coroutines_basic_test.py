"""
Generators produce data
Coroutines consume data
"""
from src.helper.ioh import captured_output, to_string


def bare_bones():
    print("My first Coroutine!")
    try:
        while True:
            value = (yield)
            print(value)
    except GeneratorExit:
        print("Exiting coroutine...")


def test_bare_bones():
    with captured_output() as(out, err):
        coroutine = bare_bones()
        # coroutines require the next() method to be called first
        next(coroutine)
        # New input can be sent with send()
        coroutine.send("First Value")
        coroutine.send("Second Value")
        # free those resources by calling close()
        # This raises a GeneratorExit exception that needs to be dealt with
        coroutine.close()
    assert to_string(out) == """\
My first Coroutine!
First Value
Second Value
Exiting coroutine..."""
