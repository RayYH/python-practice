from src.core.oop.triangle import Triangle, Polygon
from src.helper.io import captured_output, to_string
import io


def test_triangle(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('2\n3\n4'))
    t = Triangle()
    t.input_sides()
    with captured_output() as (out, err):
        t.display_sides()
    assert to_string(out) == '''Side 1 is 2.0
Side 2 is 3.0
Side 3 is 4.0'''
    assert '{:.2f}'.format(t.get_area()) == '2.90'
    assert isinstance(t, Triangle)
    assert isinstance(t, Polygon)
    assert not isinstance(t, int)
    assert isinstance(t, object)
    assert not issubclass(Polygon, Triangle)
    assert issubclass(Triangle, Polygon)
    assert issubclass(bool, int)
