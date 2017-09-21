import math

class Sphere():
    def __init__(self, radius = 0):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_volume(self):
        return  4/3 * math.pi * self.radius**3