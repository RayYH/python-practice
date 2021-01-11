from src.helper.ioh import captured_output, to_string
import os


# parent class
class Bird:
    name = "Bird"

    def __init__(self):
        print("Bird is ready")

    def who_is_this(self):
        print("Bird")
        print(self.name)

    def swim(self):
        print("Bird")
        print(self.name + " swim faster")


# child class - use SubClass(BaseClass) instead of extends keyword
class Penguin(Bird):
    name = "Penguin"

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def who_is_this(self):
        print("Penguin")
        print(self.name)

    def run(self):
        print("Penguin")
        print(self.name + " run faster")


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


def test_multiple_inheritance_mro():
    current_file = os.path.splitext(os.path.basename(__file__))[0] + '.'
    # Method Resolution Order (MRO)
    assert '{}'.format(M.mro()) \
               .replace("class ", "") \
               .replace(current_file, "") \
           == "[<'M'>, <'B'>, <'A'>, <'X'>, <'Y'>, <'Z'>, <'object'>]"


def test_penguin():
    with captured_output() as (out, err):
        peggy = Penguin()
        # Bird is ready
        # Penguin is ready
        peggy.who_is_this()
        # Penguin
        # Penguin
        peggy.swim()
        # Bird
        # Penguin swim faster
        peggy.run()
        # Penguin
        # Penguin run faster
    assert to_string(out) == '''Bird is ready
Penguin is ready
Penguin
Penguin
Bird
Penguin swim faster
Penguin
Penguin run faster'''
