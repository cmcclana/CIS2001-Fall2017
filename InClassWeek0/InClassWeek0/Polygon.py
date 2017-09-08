class Polygon(object):
    """description of class"""
    def __init__(self, name, number_of_sides):
        self._name = name
        self._number_of_sides = number_of_sides
    
    def get_area(self):
        """returns the area of the polygon"""

    def get_perimeter(self):
        return 0

    def get_name(self):
        return self._name

    def get_number_of_sides(self):
        return self._number_of_sides

    def __str__(self):
        return "I'm a poly named: " + self._name