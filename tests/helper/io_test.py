from src.helper.io import captured_output


def foo():
    print('foo')


def test_captured_output():
    with captured_output() as (out, err):
        foo()
    output = out.getvalue().strip()
    assert output == 'foo'
