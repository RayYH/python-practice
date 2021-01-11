"""
In Python, we denote private attributes using underscore as the prefix i.e
single _ or double __.
"""


class Computer:
    def __init__(self):
        self.__max_price = 900

    def sell(self):
        return "Selling Price: {}".format(self.__max_price)

    def set_max_price(self, price):
        self.__max_price = price


def test_computer():
    c = Computer()
    assert c.sell() == 'Selling Price: 900'

    # change the price - not working!
    c.__max_price = 1000
    assert c.sell() == 'Selling Price: 900'

    # using setter function - now works!
    c.set_max_price(1000)
    assert c.sell() == 'Selling Price: 1000'


# Name mangling is helpful for letting subclasses override methods without
# breaking exist method calls.
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):
    # noinspection PyMethodOverriding
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


def test_override_methods():
    mapping = Mapping([])
    mapping.update([1, 2, 3])
    assert mapping.items_list == [1, 2, 3]
    mapping_subclass = MappingSubclass([])
    mapping_subclass.update(['name', 'age'], ['Ray', 25])
    assert mapping_subclass.items_list == [('name', 'Ray'), ('age', 25)]
