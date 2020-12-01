class Rect(object):
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def perimeter(self):
        return (self.__width + self.__height) * 2

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '<Rect [width: {:.2f}, height: {:.2f}]>'.format(
            self.__width, self.__height)

    def __del__(self):
        print('destroyed')
