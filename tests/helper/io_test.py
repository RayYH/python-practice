from src.helper.io import captured_output, to_string


def foo():
    print('foo')


def test_captured_output():
    with captured_output() as (out, err):
        foo()
    assert to_string(out) == 'foo'


def test_to_string():
    assert to_string(1) == "1"
    assert to_string(True) == "True"
