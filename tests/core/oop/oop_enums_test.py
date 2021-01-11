from enum import Enum


class Fruits(Enum):
    APPLE = 'apple'
    BANANA = 'banana'
    ORANGE = 'orange'


def test_fruits():
    assert Fruits.APPLE.value == 'apple'
    assert Fruits.BANANA.value == 'banana'
    assert Fruits.ORANGE.value == 'orange'
    for x in Fruits:
        assert x.name.lower() == x.value
