from src.core.oop.triangle import Triangle, Polygon
from src.helper.io import captured_output, to_string, stdin


# The monkeypatch fixture helps you to safely set/delete an attribute,
# dictionary item or environment variable, or to modify sys.path for importing.
def test_triangle(monkeypatch):
    stdin(monkeypatch, [2, 3, 4])
    t = Triangle()
    t.input_sides()
    with captured_output() as (out, err):
        t.display_sides()
    assert to_string(out) == '''Side 1 is 2.0
Side 2 is 3.0
Side 3 is 4.0'''
    assert '{:.2f}'.format(t.get_area()) == '2.90'
    assert '{:.2f}'.format(t.get_circumference()) == '9.00'
    assert isinstance(t, Triangle)
    assert isinstance(t, Polygon)
    assert not isinstance(t, int)
    assert isinstance(t, object)
    assert not issubclass(Polygon, Triangle)
    assert issubclass(Triangle, Polygon)
    assert issubclass(bool, int)


def test_not_valid(monkeypatch):
    stdin(monkeypatch, [1, 1, 2])
    try:
        t = Triangle()
        t.input_sides()
    except ValueError as e:
        assert str(e) == "your input parameters is invalid: check your inputs!"
