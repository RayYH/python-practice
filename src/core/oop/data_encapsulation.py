"""
In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
"""


class Computer:

    def __init__(self):
        self.__max_price = 900

    def sell(self):
        print("Selling Price: {}".format(self.__max_price))

    def set_max_price(self, price):
        self.__max_price = price


def main():
    c = Computer()
    c.sell()

    # change the price
    c.__max_price = 1000
    c.sell()

    # using setter function
    c.set_max_price(1000)
    c.sell()


if __name__ == '__main__':
    main()
