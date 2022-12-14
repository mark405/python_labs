class Rectangle:
    def __init__(self, length=1, width=1):
        self.set_length(length)
        self.set_width(width)

    def set_length(self, length):
        if isinstance(length, float | int) and 0 < length < 20:
            self.__length = length
        else:
            raise ValueError

    def set_width(self, width):
        if isinstance(width, float | int) and 0 < width < 20:
            self.__width = width
        else:
            raise ValueError

    def get_perimetr(self):
        return 2 * (self.__length + self.__width)

    def get_square(self):
        return self.__length * self.__width


try:
    rectangle = Rectangle()
    rectangle.set_length(10)
    rectangle.set_width(2.5)
    print(rectangle.get_square())
    print(rectangle.get_perimetr())
except ValueError:
    print("ValueError")

