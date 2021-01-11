"""
A scope is a textual region of a Python program where a namespace is directly
accessible. “Directly accessible” here means that an unqualified reference
to a name attempts to find the name in the namespace.

At any time during execution, there are 3 or 4 nested scopes whose namespaces
are directly accessible:

    1. the innermost scope, which is searched first, contains the local names
    2. the scopes of any enclosing functions, which are searched starting with
    the nearest enclosing scope, contains non-local, but also non-global names
    3. the next-to-last scope contains the current module’s global names
    4. the outermost scope (searched last) is the namespace containing built-in
    names

If a name is declared global, then all references and assignments go directly to
 the middle scope containing the module’s global names. To rebind variables
 found outside of the innermost scope, the nonlocal statement can be used.

The global statement can be used to indicate that particular variables live in
the global scope and should be rebound there; the nonlocal statement indicates
that particular variables live in an enclosing scope and should be rebound
there.
"""

# when we define a variable outside of a function, it is global by default.
global_string = 'global'


def get_global_string():
    return global_string


def change_global_string():
    global global_string
    global_string = 'new global'


def test_global_string():
    assert get_global_string() == 'global'
    change_global_string()
    assert get_global_string() == 'new global'


def test_nonlocal_keyword():
    # In short, nonlocal keyword lets you assign values to a variable
    # in an outer (but non-global) scope.
    def nonlocal_outer():
        x = "local"

        def nonlocal_inner():
            # This means that the variable can be neither in the local
            # nor the global scope.
            nonlocal x
            x = "nonlocal"
            assert x == "nonlocal"

        nonlocal_inner()
        assert x == "nonlocal"

    nonlocal_outer()
