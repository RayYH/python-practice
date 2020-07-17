"""
1. We can convert between different data types by using different type conversion functions like int(), str().
2. Conversion from float to int will truncate the value (make it closer to zero).
3. Conversion to and from string must contain compatible values.
4. To convert to dictionary, each element must be a pair.
"""


def test_type_conversion():
    assert int(10.1) == 10
    assert int(10.9) == 10
    assert int(-10.1) == -10
    assert int(-10.9) == -10
    assert float(5) == 5.0
    assert float('2.5') == 2.5
    assert '{} {}'.format(str(True), type(str(True))) == "True <class 'str'>"
    assert '{} {}'.format(str(2.5), type(str(2.5))) == "2.5 <class 'str'>"
    assert '{}'.format(list("string")) == "['s', 't', 'r', 'i', 'n', 'g']"
    assert '{}'.format(dict([(3, 26), (4, 44)])) == "{3: 26, 4: 44}"
    num_int = 123
    num_flo = 1.23
    num_new = num_int + num_flo
    assert '{}'.format(type(num_new)) == "<class 'float'>"
