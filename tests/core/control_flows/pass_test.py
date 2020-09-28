from src.helper.io import captured_output, to_string
from src.core.control_flows.pass_statement \
    import empty_function, EmptyClass, ClassWithEmptyMethod, pass_inside_loop


def test_empty_function():
    with captured_output() as (out, err):
        empty_function()
    assert not to_string(out)


def test_empty_class():
    with captured_output() as (out, err):
        b = EmptyClass()
        assert to_string(b)
    assert not to_string(out)


def test_class_with_empty_method():
    with captured_output() as (out, err):
        c = ClassWithEmptyMethod()
        c.fly()
    assert not to_string(out)


def test_pass_inside_loop():
    with captured_output() as (out, err):
        pass_inside_loop()
    assert to_string(out) == 'pa'
