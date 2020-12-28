from src.helper.ioh import stdin


def sum_of_two_numbers():
    a = int(input('a = '))
    b = int(input('b = '))
    return a + b


def test_sum_of_two_numbers(monkeypatch):
    stdin(monkeypatch, [2, 4])
    c = sum_of_two_numbers()
    assert c == 6
