"""
Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
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

