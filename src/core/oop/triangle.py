def check_validity(a, b, c):
    if a * b * c == 0:
        return False
    # check condition
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        # [val for _ in range(3)] returns [val, val, val]
        self.sides = [0 for _ in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]
        if not check_validity(self.sides[0], self.sides[1], self.sides[2]):
            raise ValueError('your input parameters is invalid: check your inputs!')

    def display_sides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    # __init__() in Triangle gets preference over the __init__ in Polygon.
    def __init__(self):
        Polygon.__init__(self, 3)
        # you can also use `super().__init__(3)`

    def find_area(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


def main():
    t = Triangle()
    t.input_sides()
    t.display_sides()
    t.find_area()
    assert isinstance(t, Triangle)
    assert isinstance(t, Polygon)
    assert not isinstance(t, int)
    assert isinstance(t, object)
    assert not issubclass(Polygon, Triangle)
    assert issubclass(Triangle, Polygon)
    assert issubclass(bool, int)


if __name__ == '__main__':
    main()