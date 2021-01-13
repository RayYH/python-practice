import pytest


def echo():
    while True:
        value = (yield)
        print(value)


def test_echo():
    with pytest.raises(StopIteration):
        cor = echo()
        next(cor)
        cor.close()
        cor.send("something")
