def regular_method():
    print("\n(This is a regular, non-test-case method.)")


class TestSimpleClass(object):
    """
    Classes can still be used to organize collections of test cases, with
    each test being a Method on the Class, rather than a standalone function.
    """

    x = 1
    y = 2

    def test_two_checking_method(self):
        print("\nRunning TestSimpleClass.test_twos_method")
        assert self.x != 2
        assert self.y == 2
