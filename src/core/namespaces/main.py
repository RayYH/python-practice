"""
A namespace is a collection of names.
At any given moment, there are at least three nested scopes.
1. Scope of the current function which has local names
2. Scope of the module which has global names
3. Outermost scope which has built-in names
When a reference is made inside a function, the name is searched in the local namespace,
then in the global namespace and finally in the built-in namespace.
"""


def print_hello():
    print("Hello")


def show_ids():
    """
    Everything in Python is an object.
    """
    a = 2
    print('id(2) =', id(2))
    print('id(a) =', id(a))
    a = a + 1
    print('id(a) =', id(a))
    print('id(3) =', id(3))
    # the new name b gets associated with the previous object 2.
    # This is efficient as Python does not have to create a new duplicate object.
    # This dynamic nature of name binding makes Python powerful; a name could refer to any type of object.
    # Functions are objects too, so a name can refer to them as well.
    a = print_hello
    a()
    b = 2
    print('id(b) =', id(b))
    print('id(2) =', id(2))
    # id(2) = 4389870160
    # id(a) = 4389870160
    # id(a) = 4389870192
    # id(3) = 4389870192
    # id(b) = 4389870160
    # id(2) = 4389870160


def main():
    show_ids()


if __name__ == '__main__':
    main()
