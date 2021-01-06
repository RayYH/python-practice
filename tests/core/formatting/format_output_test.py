def test_formatted_string_literals():
    year = 2016
    event = 'Referendum'
    assert f'Results of the {year} {event}' == 'Results of the 2016 Referendum'


def test_str_format_method():
    yes_votes = 42_572_654
    no_votes = 43_132_495
    percentage = yes_votes / (yes_votes + no_votes)
    assert '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage) == \
           ' 42572654 YES votes 49.67%'


def test_str_method():
    s = 'Hello, world.\n'
    assert str(s) == 'Hello, world.\n'
    f = 1 / 7
    assert str(f) == '0.14285714285714285'


def test_repr_method():
    s = 'Hello, world.\n'
    assert repr(s) == "'Hello, world.\\n'"
    f = 1 / 7
    assert repr(f) == "0.14285714285714285"
