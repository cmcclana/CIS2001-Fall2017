import unittest
from Sphere import *
import math

class Test_SphereTest(unittest.TestCase):
    def test_Sphere_get_radius(self):
        radius = 10
        sphere = Sphere(10)

        self.assertEquals(sphere.get_radius(), radius)

    def test_Sphere_get_volume(self):
        radius = 10
        sphere = Sphere(10)

        self.assertAlmostEqual( 4/3 * math.pi * radius**3, sphere.get_volume() )


if __name__ == '__main__':
    unittest.main()
