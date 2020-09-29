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
