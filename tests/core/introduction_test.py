def test_numbers():
    assert 2 + 2 == 4
    assert 50 - 5 * 6 == 20
    assert (50 - 5 * 6) / 4 == 5.0
    assert 4 * 3.75 - 1 == 14.0
    assert 8 / 5 == 1.6  # division always returns a floating point number
    assert 17 / 3 == 5.666666666666667  # classic division returns a float
    assert 17 // 3 == 5  # floor division discards the fractional part
    assert 17 % 3 == 2  # the % operator returns the remainder of the division
    assert 5 * 3 + 2 == 17  # result * divisor + remainder
    assert 5 ** 2 == 25  # 5 squared
    assert 2 ** 7 == 128  # 2 to the power of 7
    width = 20
    height = 5 * 9
    assert width * height == 900
    tax = 12.5 / 100
    price = 100.50
    assert price * tax == 12.5625
    # In interactive mode, the last printed expression is assigned to the variable _
    assert round(price + price * tax, 2) == 113.06
