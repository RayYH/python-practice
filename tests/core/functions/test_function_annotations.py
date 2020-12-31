def test_function_annotations():
    def f(ham: str, eggs: str = 'eggs') -> str:
        assert '{}'.format(f.__annotations__) == """\
{'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}"""
        return ham + ' and ' + eggs

    assert f('spam') == 'spam and eggs'
