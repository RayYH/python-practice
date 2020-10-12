class MyClass(object):
    __slots__ = ['name', 'age']

    def __init__(self):
        self.name = "Ray"
        self.age = 24


def test_my_class():
    my_class = MyClass()
    assert my_class.name == "Ray"
    assert my_class.age == 24
    my_class.name = "Tom"
    assert my_class.name == "Tom"
    try:
        print(my_class.__dict__)
    except AttributeError as ae:
        assert str(ae) == "'MyClass' object has no attribute '__dict__'"
