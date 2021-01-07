import pytest
from src.helper.ioh import captured_output, to_string
from src.core.exceptions.custom_exceptions import B, C, D, CustomException


def test_some_operations_will_throw_exceptions():
    with pytest.raises(ZeroDivisionError):
        var = 10 * (1 / 0)
        assert var
    with pytest.raises(TypeError):
        # noinspection PyTypeChecker
        var = '2' + 2
        assert var


def test_except_exceptions():
    try:
        # noinspection PyUnresolvedReferences
        4 + spam * 3
    except NameError:
        assert True


def test_custom_exceptions():
    with captured_output() as (out, err):
        for cls in [B, C, D]:
            try:
                raise cls()
            except D:
                print('D', end='')
            except C:
                print('C', end='')
            except B:
                print('B', end='')
    # if the except clauses were reversed (with except B first),
    # it would have printed B, B, B
    assert to_string(out) == 'BCD'


def test_last_except_as():
    try:
        # noinspection PyUnresolvedReferences
        4 + spam * 3
    except NameError as e:
        assert '{}'.format(e) == "name 'spam' is not defined"


def test_except_else():
    try:
        assert True
    except NameError:
        assert False
    else:
        assert True


def test_raise_an_exception():
    try:
        raise CustomException("spam", "eggs")
    except CustomException as e:
        assert 'CustomException' in str(type(e))
        assert e.args == ('spam', 'eggs')
        assert str(e) == "('spam', 'eggs')"
        x, y = e.args
        assert x == "spam"
        assert y == "eggs"


def test_exceptions_chaining():
    with pytest.raises(RuntimeError):
        try:
            raise IOError
        except IOError as e:
            raise RuntimeError from e


def clean_up_action():
    try:
        raise KeyboardInterrupt
    finally:
        print("hello")


def test_clean_up_actions():
    with captured_output() as (out, err):
        with pytest.raises(KeyboardInterrupt):
            clean_up_action()
    assert to_string(out) == 'hello'
