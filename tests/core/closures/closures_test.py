def make_multiplier_of(n):

    def multiplier(x):
        return x * n

    return multiplier


def test_closures():
    times3 = make_multiplier_of(3)
    times5 = make_multiplier_of(5)
    assert times3(9) == 27
    assert times5(9) == 45
    # All function objects have a __closure__ attribute that
    # returns a tuple of cell objects
    # if it is a closure function.
    assert '{}'.format(times3.__closure__).startswith("(<cell at")
    assert '{}'.format(times3.__closure__).find("int object")
    # The cell object has the attribute cell_contents
    # which stores the closed value.
    assert times3.__closure__[0].cell_contents == 3
    assert times5.__closure__[0].cell_contents == 5
