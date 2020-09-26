def test_boolean_format_output():
    assert '{}'.format(type(True)) == "<class 'bool'>"
    assert '{}'.format(type(False)) == "<class 'bool'>"
    # bool value is often used in condition statements
    if True:
        assert True


def test_boolean_casts():
    assert '{}'.format(int(True)) == '1'
    assert '{}'.format(int(False)) == '0'
    assert '{}'.format(bool(1)) == 'True'
    assert '{}'.format(bool(0)) == 'False'
    assert not bool(0)
    assert not bool(0b0)
    assert not bool('')
    assert not bool([])
    assert not bool({})
    assert not bool(None)
