from src.helper.ioh import captured_output, to_string


def pass_inside_loop():
    sequence = ['p', 'a', 's', 's']
    for val in sequence:
        if val == 'p' or val == 'a':
            pass
            print(val, sep="", end="")


def test_pass_inside_loop():
    with captured_output() as (out, err):
        pass_inside_loop()
    assert to_string(out) == 'pa'


def empty_function():
    pass


def test_empty_function():
    with captured_output() as (out, err):
        empty_function()
    assert not to_string(out)


class EmptyClass:
    pass


def test_empty_class():
    with captured_output() as (out, err):
        b = EmptyClass()
        assert to_string(b)
    assert not to_string(out)


class ClassWithEmptyMethod:
    def fly(self):
        pass


def test_class_with_empty_method():
    with captured_output() as (out, err):
        c = ClassWithEmptyMethod()
        c.fly()
    assert not to_string(out)
