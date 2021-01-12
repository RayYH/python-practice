class Person(object):
    pass


class Student(Person):
    pass


def test_is_instance():
    s = Student()
    assert isinstance(s, Student)
    assert isinstance(s, Person)
    assert isinstance(s, object)
    assert not isinstance(s, int)


def test_is_subclass():
    s = Student()
    assert issubclass(s.__class__, Person)
    assert issubclass(Student, Person)
    assert issubclass(Student, object)
    assert issubclass(Person, object)
    assert issubclass(bool, int)
    assert issubclass(int, object)
    assert issubclass(bool, object)
