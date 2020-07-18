class Parrot:
    name = "Parrot"

    def fly(self):
        print(self.name + " can fly")

    def swim(self):
        print(self.name + " can't swim")


class Penguin:
    name = "Penguin"

    def fly(self):
        print(self.name + " can't fly")

    def swim(self):
        print(self.name + " can swim")


# common interface
def flying_test(bird):
    bird.fly()


# common interface
def swimming_test(bird):
    bird.swim()


def main():
    # instantiate objects
    blu = Parrot()
    peggy = Penguin()

    # passing the object
    flying_test(blu)
    flying_test(peggy)
    swimming_test(blu)
    swimming_test(peggy)


if __name__ == '__main__':
    main()
