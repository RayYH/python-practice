"""
A namespace is a mapping from names to objects, there is absolutely no relation
between names in different namespaces.

Examples:
    1. the set of built-in names
    2. the global names in a module
    3. the local names in a function invocation

Namespaces are created at different moments and have different lifetimes.

    1. The namespace containing the built-in names is created when the Python
    interpreter starts up, and is never deleted.
    2. The global namespace for a module is created when the module definition
    is read in; normally, module namespaces also last until the interpreter
    quits.
    3. The statements executed by the top-level invocation of the interpreter,
    either read from a script file or interactively, are considered part of a
    module called __main__, so they have their own global namespace.

The local namespace for a function is created when the function is called, and
deleted when the function returns or raises an exception that is not handled
within the function. Of course, recursive invocations each have their own local
namespace.
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
