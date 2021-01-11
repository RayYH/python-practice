import os


# parent class
class Bird:
    name = "Bird"

    def __init__(self):
        pass

    def who_is_this(self):
        return "{}: {}".format("Bird", self.name)

    def swim(self):
        return "{}: {} swim faster".format("Bird", self.name)


# child class - use SubClass(BaseClass) instead of extends keyword
class Penguin(Bird):
    name = "Penguin"

    def __init__(self):
        # call super() function
        super().__init__()
        pass

    def who_is_this(self):
        return "{}: {}".format("Penguin", self.name)

    def run(self):
        return "{}: {} run faster".format("Penguin", self.name)


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
    peggy = Penguin()
    assert peggy.who_is_this() == "Penguin: Penguin"
    assert peggy.swim() == "Bird: Penguin swim faster"
    assert peggy.run() == "Penguin: Penguin run faster"
