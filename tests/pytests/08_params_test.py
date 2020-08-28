import pytest


def test_parameterization(letter):
    print("\n   Running test_parameterization with {}".format(letter))


def test_modes(mode):
    print("\n   Running test_modes with {}".format(mode))


def test_users(user):
    print("\n   Running test_users with {}".format(user))


@pytest.fixture(params=["a", "b", "c", "d", "e"])
def letter(request):
    """
    Fixtures with parameters will run once per param
    (You can access the current param via the request fixture)
    """
    yield request.param


@pytest.fixture(params=[1, 2, 3], ids=['foo', 'bar', 'baz'])
def mode(request):
    """
    Fixtures with parameters will run once per param
    (You can access the current param via the request fixture)
    """
    yield request.param


@pytest.fixture(params=[{"name": "Ray", "age": 23}, {"name": "Bob", "age": 24}])
def user(request):
    """
    Fixtures with parameters will run once per param
    (You can access the current param via the request fixture)
    """
    yield request.param
