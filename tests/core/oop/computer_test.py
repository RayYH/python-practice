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
