from Rectangle import Rectangle

class Square(Rectangle):
    """description of class"""

    def __init__(self, name, number_of_sides, length):
        super().__init__(name, number_of_sides, length, length)


