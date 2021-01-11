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
