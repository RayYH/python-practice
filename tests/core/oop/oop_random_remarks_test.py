class Warehouse:
    purpose = 'storage'
    region = 'west'


def test_attribute_lookup_prioritizes():
    w1 = Warehouse()
    assert w1.purpose == 'storage'
    assert w1.region == 'west'
    w2 = Warehouse()
    w2.region = 'east'
    assert w2.purpose == 'storage'
    assert w2.region == 'east'


def min_f(self, x, y):
    assert self
    return min(x, y)


class C:
    f = min_f

    def g(self):
        assert self
        return 'hello'

    h = g


def test_c():
    c = C()
    # noinspection PyArgumentList
    assert c.f(1, 2) == 1
    assert c.h() == 'hello'
    assert C.h(c) == 'hello'
