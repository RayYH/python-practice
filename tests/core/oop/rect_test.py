from src.core.oop.rect import Rect
from src.helper.ioh import captured_output, to_string


def test_rect():
    rect = Rect(2, 5)
    assert rect.perimeter() == 14
    assert rect.area() == 10
    assert str(rect) == '<Rect [width: 2.00, height: 5.00]>'
    with captured_output() as (out, err):
        del rect
    assert to_string(out) == 'destroyed'
