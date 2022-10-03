class Rectangle(object):
    def __init__(self):
        self.__length = 1.
        self.__width = 1.

    def set_length(self, length):
        if isinstance(length, float) and 0.0 < length < 20.0:
            self.__length = length
        else:
            print("Invalid length")

    def set_width(self, width):
        if isinstance(width, float) and 0.0 < width < 20.0:
            self.__length = width
        else:
            print("Invalid length")

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_perimetr(self):
        return 2 * (self.__length + self.__width)

    def get_square(self):
        return self.__length * self.__width


rectangle = Rectangle()

rectangle.set_length(2.3)
rectangle.set_width(2.5)

print(rectangle.get_square())
print(rectangle.get_perimetr())
