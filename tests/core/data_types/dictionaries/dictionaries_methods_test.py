def test_basic_operations():
    my_dict = {'name': 'Jack', 'age': 26}
    assert my_dict['name'] == 'Jack'
    del my_dict['name']
    assert my_dict == {'age': 26}
    del my_dict


def test_builtin_functions():
    marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
    squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
    assert marks == {'English': 0, 'Math': 0, 'Science': 0}
    assert list(sorted(marks.keys())) == ['English', 'Math', 'Science']
    assert not all(squares)
    assert any(squares)
    assert len(squares) == 6
    assert sorted(squares) == [0, 1, 3, 5, 7, 9]


def test_get():
    my_dict = {'name': 'Jack', 'age': 26}
    assert my_dict.get('name') == 'Jack'
    assert my_dict.get('age') == 26


def test_pop():
    my_dict = {'name': 'Jack', 'age': 26}
    assert my_dict.pop('name') == 'Jack'
    assert my_dict == {'age': 26}


def test_copy():
    my_dict = {'name': 'Jack', 'age': 26}
    my_dict_reference = my_dict
    my_dict_duplicate = my_dict.copy()
    my_dict['name'] = 'Ray'
    assert my_dict_reference['name'] == 'Ray'
    assert my_dict_duplicate['name'] == 'Jack'


def test_clear():
    my_dict = {'name': 'Jack', 'age': 26}
    my_dict.clear()
    assert len(my_dict) == 0


def test_keys():
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    dict_keys = car.keys()
    car["color"] = "white"
    assert '{}'.format(
        dict_keys) == "dict_keys(['brand', 'model', 'year', 'color'])"


def test_values():
    my_dict = {'name': 'Jack', 'age': 26}
    assert '{}'.format(my_dict.values()) == \
           "dict_values(['Jack', 26])"


def test_items():
    my_dict = {'name': 'Jack', 'age': 26}
    assert '{}'.format(my_dict.items()) == \
           "dict_items([('name', 'Jack'), ('age', 26)])"


def test_fromkeys():
    keys = ["one", "two", "three"]
    assert dict.fromkeys(keys, 1) == {"one": 1, "two": 1, "three": 1}
    keys = ("four", "five", "six")
    assert dict.fromkeys(keys) == {"four": None, "five": None, "six": None}


def test_popitem():
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    assert car.popitem() == ('year', 1964)
    assert car == {'brand': 'Ford', 'model': 'Mustang'}


def test_set_default():
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    # model key exists
    assert car.setdefault("model", "Bronco") == "Mustang"
    # color key does not exist
    assert car.setdefault("color", "White") == "White"
    assert car == {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "color": "White"
    }


def test_update():
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    car.update({"color": "White"})
    assert car == {'brand': 'Ford', 'model': 'Mustang', 'year': 1964,
                   'color': 'White'}

    car.update({"color": "Black", "year": 1976})
    assert car == {'brand': 'Ford', 'model': 'Mustang', 'year': 1976,
                   'color': 'Black'}
