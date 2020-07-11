"""
https://pyformat.info/
"""


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
    assert '%10s' % ('test',) == string
    assert '{:>10}'.format('test') == string
    string = 'test      '
    assert '%-10s' % ('test',) == string
    assert '{:10}'.format('test') == string
    string = 'test______'
    assert '{:_<10}'.format('test') == string
    string = '   test   '
    assert '{:^10}'.format('test') == string
    string = ' zip  '
    assert '{:^6}'.format('zip') == string


def test_truncate_long_string():
    string = 'hello'
    assert '%.5s' % ('hello world',) == string
    assert '{:.5}'.format('hello world') == string
    string = 'hello     '
    assert '%-10.5s' % ('hello world',) == string
    assert '{:10.5}'.format('hello world') == string
