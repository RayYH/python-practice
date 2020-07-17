"""
When we define a variable outside of a function, it is global by default. You don't have to use global keyword.
"""
global_string = 'global'


def get_global_string():
    return global_string


def change_global_string():
    global global_string
    global_string = 'new global'


def test_nonlocal_keyword():
    """
    In short, nonlocal keyword lets you assign values to a variable in an outer (but non-global) scope.
    """

    def nonlocal_outer():
        x = "local"

        def nonlocal_inner():
            # This means that the variable can be neither in the local nor the global scope.
            nonlocal x
            x = "nonlocal"
            assert x == "nonlocal"

        nonlocal_inner()
        assert x == "nonlocal"

    nonlocal_outer()


def test_global_string():
    assert get_global_string() == 'global'
    change_global_string()
    assert get_global_string() == 'new global'
