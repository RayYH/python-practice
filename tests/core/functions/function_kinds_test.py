from src.helper.sysh import python_version
from src.helper.disable_inspection import do_whatever
import pytest


def test_standard_arg():
    def standard_arg(arg):
        return arg

    assert standard_arg(2) == 2
    assert standard_arg(arg=2) == 2


def test_keyword_only_arg():
    def kwd_only_arg(*, arg):
        return arg

    assert kwd_only_arg(arg=3) == 3
    with pytest.raises(TypeError):
        # noinspection PyArgumentList
        kwd_only_arg(3)


def test_positional_only_arg():
    if python_version() >= 380:
        # noinspection PyCompatibility
        def pos_only_arg(arg, /):
            return arg

        assert pos_only_arg(1) == 1
        with pytest.raises(TypeError):
            # noinspection PyArgumentList
            pos_only_arg(arg=1)


def test_combined():
    if python_version() >= 380:
        # noinspection PyCompatibility
        def combined(pos_only, /, standard, *, kwd_only):
            return [pos_only, standard, kwd_only]

        with pytest.raises(TypeError):
            # noinspection PyArgumentList
            combined(1, 2, 3)

        with pytest.raises(TypeError):
            # noinspection PyArgumentList
            combined(pos_only=1, standard=2, kwd_only=3)

        assert combined(1, 2, kwd_only=3) == [1, 2, 3]
        assert combined(1, standard=2, kwd_only=3) == [1, 2, 3]


def test_has_property():
    def check(name, **kwargs):
        do_whatever(name)
        return 'name' in kwargs

    with pytest.raises(TypeError):
        check(1, **{'name': "Ray"})

    # noinspection PyCompatibility
    def check(name, /, **kwargs):
        do_whatever(name)
        return 'name' in kwargs

    assert check(1, **{'name': "Ray"})
    assert not check(1, **{'age': 24})
