from Polygon import Polygon

class Rectangle(Polygon):
    """description of class"""

    def __init__(self, name, number_of_sides, length, width):
        Polygon.__init__(self, name, number_of_sides)
        self._length = length
        self._width = width

    def get_area(self):
        return self._length * self._width

    def get_perimeter(self):
        return self._length * 2 + self._width * 2

    def __str__(self):
        return super().__str__() + " area: " + str(self.get_area()) + " perimeter: " + str(self.get_perimeter())



