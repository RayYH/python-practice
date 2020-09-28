from src.core.oop.polymorphism \
    import Parrot, Penguin, flying_test, swimming_test


def test_polymorphism():
    # instantiate objects
    blu = Parrot()
    peggy = Penguin()
    # passing the object
    assert flying_test(blu) == "Parrot can fly"
    assert flying_test(peggy) == "Penguin can't fly"
    assert swimming_test(blu) == "Parrot can't swim"
    assert swimming_test(peggy) == "Penguin can swim"
