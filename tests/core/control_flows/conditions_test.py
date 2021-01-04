class Person:
    pass


class Student(Person):
    pass


class Book:
    pass


def test_in():
    assert 'a' in ['a', 'b', 'c']
    assert 'd' not in ['a', 'b', 'c']


def test_is():
    person = Person()
    person_ref = person
    student = Student()
    book = Book()
    assert person is not student
    assert student is not person
    assert book is not student
    assert person is person_ref


def test_chained_comparisons():
    assert 1 < 2 == 2
    assert 1 == 1 == 1 == 1
    assert 1 < 2 < 3 < 4 < 5
    assert 1 < 2 < 3 > 2
    assert 1 < 2 != 3 == 3 < 4 < 5 > 4


def test_short_circuit_operators():
    string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
    non_null = string1 or string2 or string3
    assert non_null == 'Trondheim'
    age = '' and 25
    assert not age


def test_comparing_sequences():
    assert (1, 2, 3) < (1, 2, 4)
    assert [1, 2, 3] < [1, 2, 4]
    assert 'ABC' < 'C' < 'Pascal' < 'Python'
    assert (1, 2, 3, 4) < (1, 2, 4)
    assert (1, 2) < (1, 2, -1)
    assert (1, 2, 3) == (1.0, 2.0, 3.0)
    assert (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
