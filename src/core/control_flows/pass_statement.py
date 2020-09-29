def pass_inside_loop():
    sequence = ['p', 'a', 's', 's']
    for val in sequence:
        if val == 'p' or val == 'a':
            pass
            print(val, sep="", end="")


def empty_function():
    pass


class EmptyClass:
    pass


class ClassWithEmptyMethod:
    def fly(self):
        pass
