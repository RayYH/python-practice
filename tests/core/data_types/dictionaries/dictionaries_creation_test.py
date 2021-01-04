import pytest


def test_keys_can_be_any_immutable_types():
    my_dict = {}
    assert len(my_dict) == 0

    # numbers
    my_dict[1] = 1
    assert my_dict.get(1) == 1

    # strings
    my_dict["name"] = "Ray"
    assert my_dict.get("name") == "Ray"

    # tuples
    my_dict[("python", "programming")] = "Awesome"
    assert my_dict[("python", "programming")] == "Awesome"
    my_dict[(2, 3)] = "Prime Factors"
    assert my_dict[(2, 3)] == "Prime Factors"
    my_dict[("Ray", 25)] = "mixed"
    assert my_dict[("Ray", 25)] == "mixed"


def test_keys_cannot_be_mutable_types():
    my_dict = {}
    assert len(my_dict) == 0
    with pytest.raises(TypeError) as e:
        my_dict[[]] = "empty"
        assert str(e).startswith("unhashable")


def test_dictionaries_from_literals():
    tel = {'jack': 4098, 'sape': 4139}
    assert tel
    tel['guido'] = 4127
    assert tel == {'jack': 4098, 'sape': 4139, 'guido': 4127}


def test_dictionaries_from_key_value_pairs():
    assert dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) == \
           {'sape': 4139, 'guido': 4127, 'jack': 4098}


def test_dictionaries_comprehensions():
    assert {x: x ** 2 for x in (2, 4, 6)} == \
           {2: 4, 4: 16, 6: 36}
    assert {x: x * x for x in range(11) if x % 2 == 1} == \
           {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}


def test_dictionaries_from_keyword_arguments():
    assert dict(sape=4139, guido=4127, jack=4098) == \
           {'sape': 4139, 'guido': 4127, 'jack': 4098}
