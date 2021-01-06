from datetime import datetime


class Data(object):
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]


class HAL9000(object):
    def __format__(self, custom_format):
        if custom_format == 'open-the-pod-bay-doors':
            return "I'm afraid I can't do that."
        return 'HAL 9000'


def test_format_fields():
    assert '%s %s' % ('one', 'two') == "one two"
    assert '{} {}'.format('one', 'two') == "one two"


def test_format_fields_with_position_indexes():
    # % does not support this
    assert '{1} {0}'.format('two', 'one') == "one two"


def test_formatting_integers():
    assert '%d %d' % (1, 2) == '1 2'
    assert '{} {}'.format(1, 2) == '1 2'


def test_str_and_repr_methods_called_on_objects():
    assert '%s %r' % (Data(), Data()) == 'str repr'
    assert '{0!s} {0!r}'.format(Data()) == 'str repr'


def test_padding_and_aligning_strings():
    # align right
    assert '%10s' % ('test', ) == '      test'
    assert '{:>10}'.format('test') == '      test'
    # align left
    assert '%-10s' % ('test', ) == 'test      '
    assert '{:10}'.format('test') == 'test      '
    # choose the padding character
    assert '{:_<10}'.format('test') == 'test______'
    assert '{:_>10}'.format('test') == '______test'
    # center align
    assert '{:^10}'.format('test') == '   test   '
    assert '{:^6}'.format('zip') == ' zip  '
    assert '{:_^6}'.format('zip') == '_zip__'


def test_truncating_long_string():
    # The number behind a . in the format specifies the precision of the
    # output. For strings that means that the output is truncated to
    # the specified length.
    assert '%.5s' % ('hello world', ) == 'hello'
    assert '{:.5}'.format('hello world') == 'hello'
    # It is also possible to combine truncating and padding
    assert '%-10.5s' % ('hello world', ) == 'hello     '
    assert '{:10.5}'.format('hello world') == 'hello     '


def test_numbers():
    # decimal
    assert '%d' % (42, ) == '42'
    assert '{:d}'.format(42) == '42'
    # float
    assert '%f' % (3.141592653589793, ) == "3.141593"
    assert '{:f}'.format(3.141592653589793) == "3.141593"
    # float with precision
    assert '%.2f' % (3.141592653589793, ) == "3.14"
    assert '{:.2f}'.format(3.141592653589793) == "3.14"


def test_padding_numbers():
    # padding with blank character
    assert '%4d' % (42, ) == "  42"
    assert '{:4d}'.format(42) == "  42"
    # padding with 0
    assert '%06.2f' % (3.141592653589793, ) == "003.14"
    assert '{:06.2f}'.format(3.141592653589793) == "003.14"
    assert '%04d' % (42, ) == "0042"
    assert '{:04d}'.format(42) == "0042"


def test_signed_numbers():
    # by default only negative numbers are prefixed with a sign
    assert '%d' % (-23) == "-23"
    assert '%d' % (42, ) == "42"
    assert '{:d}'.format(-23) == "-23"
    assert '{:d}'.format(42) == "42"
    # positive numbers prefixed with a + sign
    assert '%+d' % (42, ) == "+42"
    assert '{:+d}'.format(42) == "+42"
    # negative numbers prefixed with a - sign
    # positive numbers prefixed with a leading space
    assert '% d' % ((-23), ) == "-23"
    assert '% d' % (42, ) == " 42"
    assert '% d' % (+42, ) == " 42"
    assert '{: d}'.format((-23)) == "-23"
    assert '{: d}'.format(42) == " 42"
    assert '{: d}'.format(+42) == " 42"
    # New style formatting is also able to control the position of the sign
    # symbol relative to the padding.
    assert '{:=5d}'.format((-23)) == "-  23"
    assert '{:=+5d}'.format(23) == "+  23"
    assert '{:= 5d}'.format(23) == "   23"


def test_named_placeholders():
    data = {'first': 'Hello', 'last': 'World!'}
    string = "Hello World!"
    assert '%(first)s %(last)s' % data == string
    assert '{first} {last}'.format(**data) == string
    assert '{first} {last}'.format(first='Hello', last='World!') == string


def test_getitem_and_getattr():
    person = {'first': 'Ray', 'last': 'Hong'}
    assert '{p[first]} {p[last]}'.format(p=person) == "Ray Hong"
    data = [4, 8, 15, 16, 23, 42]
    assert '{d[4]} {d[5]}'.format(d=data) == "23 42"
    assert '{p.type}'.format(p=Plant()) == "tree"
    assert '{p.type}: {p.kinds[0][name]}'.format(p=Plant()) == "tree: oak"


def test_datetime():
    # see https://docs.python.org/3/library/datetime.html
    date = datetime(2001, 2, 3, 4, 5, 18)
    assert '{:%Y-%m-%d %H:%M:%S}'.format(date) == "2001-02-03 04:05:18"


def test_parametrized_formats():
    # same as '%5.2f' % (2.7182)
    assert '%*.*f' % (5, 2, 2.7182) == " 2.72"
    assert '{:{align}{width}}'.format('test', align='^', width='10') == \
           "   test   "
    assert '{:{width}.{precision}f}'.format(2.7182, width=5, precision=2) == \
           " 2.72"
    assert '{:{precision}} = {:{precision}}'.format('Gibberish',
                                                    2.7182, precision='.3') \
           == "Gib = 2.72"
    dt = datetime(2001, 2, 3, 4, 5)
    assert '{:{date_format} {time_format}}'.format(
        dt, date_format='%Y-%m-%d', time_format='%H:%M') == "2001-02-03 04:05"
    assert '{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3) == "     +2.72"
    assert '{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3,
                                     sign='+') == "     +2.72"


def test_custom_objects():
    assert '{:open-the-pod-bay-doors}'.format(
        HAL9000()) == "I'm afraid I can't do that."
