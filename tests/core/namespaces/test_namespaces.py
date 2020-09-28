"""
A namespace is a collection of names.
At any given moment, there are at least three nested scopes.
1. Scope of the current function which has local names
2. Scope of the module which has global names
3. Outermost scope which has built-in names

When a reference is made inside a function, the name is searched in the local
namespace, then in the global namespace and finally in the built-in namespace.
"""


def get_greet_str():
    return "Hello!"


def test_everything_in_python_is_an_object():
    """
    Everything in Python is an object.
    """
    a = 2
    assert id(2) == id(a)
    a = a + 1
    assert id(3) == id(a)
    # the new name b gets associated with the previous object 2.
    # This is efficient as Python does not have to create
    # a new duplicate object. a name could refer to any type of object.
    # Functions are objects too, so a name can refer to them as well.
    a = get_greet_str
    assert a() == "Hello!"
    b = 2
    assert id(b) == id(2)
