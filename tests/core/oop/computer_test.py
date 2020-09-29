from src.core.oop.computer import Computer


def test_computer():
    c = Computer()
    assert c.sell() == 'Selling Price: 900'

    # change the price - not working!
    c.__max_price = 1000
    assert c.sell() == 'Selling Price: 900'

    # using setter function - now works!
    c.set_max_price(1000)
    assert c.sell() == 'Selling Price: 1000'
