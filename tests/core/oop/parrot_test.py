from src.core.oop.parrot import Parrot


def test_class_objects():
    blu = Parrot("Blu", 10)
    woo = Parrot("Woo", 15)
    assert blu.__class__.species == 'bird'
    assert woo.__class__.species == 'bird'
    assert blu.name == 'Blu'
    assert blu.age == 10
    assert woo.name == "Woo"
    assert woo.age == 15
    assert blu.sing("'Happy'") == "Blu sings 'Happy'"
    assert blu.dance() == "Blu is now dancing"
