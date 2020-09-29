"""
https://pyformat.info/

You should use new method 'string'.format(...) instead of % operator
"""
from datetime import datetime


class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]


class HAL9000(object):
    def __format__(self, custom_format):
        if custom_format == 'open-the-pod-bay-doors':
            return "I'm afraid I can't do that."
        return 'HAL 9000'


class Data(object):
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


def test_basic_formatting():
    string = "one two"
    assert '%s %s' % ('one', 'two') == string
    assert '{} {}'.format('one', 'two') == string
    assert '{1} {0}'.format('two', 'one') == string
    string = '1 2'
    assert '%d %d' % (1, 2) == string
    assert '{} {}'.format(1, 2) == string


def test_value_conversion():
    string = "str repr"
    assert '%s %r' % (Data(), Data()) == string
    assert '{0!s} {0!r}'.format(Data()) == string


def test_padding_and_aligning_strings():
    string = '      test'
    assert '%10s' % ('test', ) == string
    assert '{:>10}'.format('test') == string
    string = 'test      '
    assert '%-10s' % ('test', ) == string
    assert '{:10}'.format('test') == string
    string = 'test______'
    assert '{:_<10}'.format('test') == string
    string = '   test   '
    assert '{:^10}'.format('test') == string
    string = ' zip  '
    assert '{:^6}'.format('zip') == string


def test_truncate_long_string():
    string = 'hello'
    assert '%.5s' % ('hello world', ) == string
    assert '{:.5}'.format('hello world') == string
    string = 'hello     '
    assert '%-10.5s' % ('hello world', ) == string
    assert '{:10.5}'.format('hello world') == string


def test_numbers():
    string = "42"
    assert '%d' % (42, ) == string
    assert '{:d}'.format(42) == string
    string = "3.141593"
    assert '%f' % (3.141592653589793, ) == string
    assert '{:f}'.format(3.141592653589793) == string


def test_padding_numbers():
    string = "  42"
    assert '%4d' % (42, ) == string
    assert '{:4d}'.format(42) == string
    string = "003.14"
    assert '%06.2f' % (3.141592653589793, ) == string
    assert '{:06.2f}'.format(3.141592653589793) == string
    string = "0042"
    assert '%04d' % (42, ) == string
    assert '{:04d}'.format(42) == string


def test_signed_numbers():
    string = "+42"
    assert '%+d' % (42, ) == string
    assert '{:+d}'.format(42) == string
    string = "-23"
    assert '% d' % ((-23), ) == string
    assert '{: d}'.format((-23)) == string
    string = " 42"
    assert '% d' % (42, ) == string
    assert '{: d}'.format(42) == string
    string = "-  23"
    assert '{:=5d}'.format((-23)) == string
    string = "+  23"
    assert '{:=+5d}'.format(23) == string


def test_named_placeholders():
    data = {'first': 'Hello', 'last': 'World!'}
    string = "Hello World!"
    assert '%(first)s %(last)s' % data == string
    assert '{first} {last}'.format(**data) == string
    assert '{first} {last}'.format(first='Hello', last='World!') == string


def test_getitem_and_getattr():
    person = {'first': 'Ray', 'last': 'Hong'}
    string = "Ray Hong"
    assert '{p[first]} {p[last]}'.format(p=person) == string
    data = [4, 8, 15, 16, 23, 42]
    string = "23 42"
    assert '{d[4]} {d[5]}'.format(d=data) == string
    assert '{p.type}'.format(p=Plant()) == "tree"
    assert '{p.type}: {p.kinds[0][name]}'.format(p=Plant()) == "tree: oak"


def test_datetime():
    assert '{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4,
                                               5)) == "2001-02-03 04:05"


def test_parametrized_formats():
    assert '%*.*f' % (5, 2, 2.7182) == " 2.72"
    assert '{:{align}{width}}'.format('test', align='^',
                                      width='10') == "   test   "
    assert '{:{width}.{precision}f}'.format(2.7182, width=5,
                                            precision=2) == " 2.72"
    assert '{:{precision}} = {:{precision}}'.format(
        'Gibberish', 2.7182, precision='.3') == "Gib = 2.72"

    dt = datetime(2001, 2, 3, 4, 5)
    assert '{:{date_format} {time_format}}'.format(
        dt, date_format='%Y-%m-%d', time_format='%H:%M') == "2001-02-03 04:05"
    assert '{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3) == "     +2.72"
    assert '{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3,
                                     sign='+') == "     +2.72"


def test_custom_objects():
    assert '{:open-the-pod-bay-doors}'.format(
        HAL9000()) == "I'm afraid I can't do that."
