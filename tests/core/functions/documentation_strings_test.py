def test_documentation_strings():
    def my_func():
        """
        Do nothing, but document it.
        No, really, it doesn't do anything.
        """
        pass

    assert my_func.__doc__ == """
        Do nothing, but document it.
        No, really, it doesn't do anything.
        """
