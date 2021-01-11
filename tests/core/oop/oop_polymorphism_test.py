"""
Polymorphism is an ability (in OOP) to use a common interface
for multiple forms (data types).
"""


class Parrot:
    name = "Parrot"

    def fly(self):
        return self.name + " can fly"

    def swim(self):
        return self.name + " can't swim"


class Penguin:
    name = "Penguin"

    def fly(self):
        return self.name + " can't fly"

    def swim(self):
        return self.name + " can swim"


# common interface
def flying_test(bird):
    return bird.fly()


# common interface
def swimming_test(bird):
    return bird.swim()


def test_polymorphism():
    # instantiate objects
    blu = Parrot()
    peggy = Penguin()
    # passing the object
    assert flying_test(blu) == "Parrot can fly"
    assert flying_test(peggy) == "Penguin can't fly"
    assert swimming_test(blu) == "Parrot can't swim"
    assert swimming_test(peggy) == "Penguin can swim"
