import pytest
import operator


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def test_append():
    fruits = ['orange', 'apple']
    assert fruits
    fruits.append('pear')
    assert fruits == ['orange', 'apple', 'pear']


def test_extend():
    fruits = ['orange']
    assert fruits
    fruits.extend(['apple', 'pear'])
    assert fruits == ['orange', 'apple', 'pear']


def test_insert():
    fruits = []
    assert not fruits
    fruits.insert(0, 'orange')
    fruits.insert(1, 'apple')
    assert fruits == ['orange', 'apple']
    fruits.insert(999, 'apple')
    assert fruits == ['orange', 'apple', 'apple']
    fruits.insert(len(fruits), 'banana')
    assert fruits == ['orange', 'apple', 'apple', 'banana']
    fruits.insert(-2, 'pear')
    assert fruits == ['orange', 'apple', 'pear', 'apple', 'banana']


def test_remove():
    fruits = ['orange', 'apple', 'pear', 'orange', 'apple', 'pear']
    fruits.remove('orange')
    assert fruits == ['apple', 'pear', 'orange', 'apple', 'pear']
    with pytest.raises(ValueError):
        fruits.remove('value_not_exists')


def test_pop():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits
    fruits.pop()
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']
    fruits.pop(0)
    assert fruits == ['apple', 'pear', 'banana', 'kiwi', 'apple']
    fruits.pop(-1)
    assert fruits == ['apple', 'pear', 'banana', 'kiwi']


def test_clear():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits
    fruits.clear()
    assert not fruits


def test_index():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits
    assert fruits.index('orange') == 0
    assert fruits.index('banana') == 3
    assert fruits.index('banana', 4) == 6
    with pytest.raises(ValueError):
        assert fruits.index('banana', 0, 2)


def test_count():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits.count('apple') == 2
    assert fruits.count('tangerine') == 0


def test_sort():
    fruits = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange',
              'grape']
    assert fruits
    fruits.sort()
    assert fruits == ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi',
                      'orange', 'pear']
    fruits.sort(reverse=True)
    assert fruits == ['pear', 'orange', 'kiwi', 'grape', 'banana', 'banana',
                      'apple', 'apple']
    users = [
        {'name': 'Bob', 'age': 32},
        {'name': 'Ray', 'age': 24},
        {'name': "Mary", 'age': 12}
    ]
    users.sort(key=lambda x: x['name'])
    assert users == [
        {'age': 32, 'name': 'Bob'},
        {'age': 12, 'name': 'Mary'},
        {'age': 24, 'name': 'Ray'}
    ]
    assert sorted("This is a test string from Andrew".split(), key=str.lower) \
           == ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

    ray = User(name="Ray", age=24)
    mary = User(name="Mary", age=12)
    bob = User(name="Bob", age=32)
    users = [ray, mary, bob]
    users.sort(key=operator.attrgetter('age'))
    assert users == [mary, ray, bob]


def test_reverse():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits.reverse()
    assert fruits == \
           ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
    assert fruits[::-1] == \
           ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


def test_copy():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits1 = fruits
    fruits.pop()
    assert fruits1 == fruits
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits1 = fruits.copy()
    fruits2 = fruits[:]
    fruits.pop()
    assert fruits != fruits1
    fruits1.pop()
    assert fruits1 != fruits2
