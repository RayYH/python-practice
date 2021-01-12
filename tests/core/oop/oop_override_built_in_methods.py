from src.helper.ioh import captured_output, to_string


class Rect(object):
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def perimeter(self):
        return (self.__width + self.__height) * 2

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '<Rect [width: {:.2f}, height: {:.2f}]>' \
            .format(self.__width, self.__height)

    def __repr__(self):
        return 'Rect(width={:.2f}, height={:.2f})' \
            .format(self.__width, self.__height)

    def __del__(self):
        print('destroyed')


def test_rect():
    rect = Rect(2, 5)
    assert rect.perimeter() == 14
    assert rect.area() == 10
    assert str(rect) == '<Rect [width: 2.00, height: 5.00]>'
    assert repr(rect) == 'Rect(width=2.00, height=5.00)'
    with captured_output() as (out, err):
        del rect
    assert to_string(out) == 'destroyed'
