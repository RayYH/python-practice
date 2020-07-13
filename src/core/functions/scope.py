# When we define a variable outside of a function, it is global by default. You don't have to use global keyword.
global_string = 'global'


def show_global_string():
    print('global_string inside show_global_string function:', global_string)


def change_global_string():
    global global_string
    global_string = 'changed by change_global_string'
    print('global_string:', global_string)


def nonlocal_outer():
    x = "local"

    def nonlocal_inner():
        # This means that the variable can be neither in the local nor the global scope.
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    nonlocal_inner()
    print("outer:", x)


def main():
    show_global_string()
    print('global_string inside main function:', global_string)
    change_global_string()
    print('global_string inside main function:', global_string)
    nonlocal_outer()


if __name__ == '__main__':
    main()
