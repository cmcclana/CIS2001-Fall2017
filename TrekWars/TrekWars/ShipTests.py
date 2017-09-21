import unittest
from Ship import *

class Test_ShipTests(unittest.TestCase):
    def setUp(self):
        self.name = "Boaty McBoat Face"
        self.x = 1
        self.y = 2
        self.alignment = "something"
        self.max_health = 10
        self.range = 5
        self.attack_power = 20
        self.damage = 10
        
        self.first = Ship(self.name, self.x, self.y, self.alignment, 
                          self.max_health, self.range, self.attack_power)
    
    def test_Ship_init(self):
        self.assertEquals(self.name, self.first.name)
        self.assertEquals(self.x, self.first.x_location)
        self.assertEquals(self.y, self.first.y_location)

    def test_ship_assess_damage(self):
        self.first.assess_damage(self.damage)

        self.assertEquals(self.max_health - self.damage, self.first.current_health )

    def test_ship_assess_damage_doesnt_go_below_zero(self):
        
        self.first.assess_damage(20)

        self.assertEquals(0, self.first.current_health )

    def test_ship_assess_damage_doesnt_go_above_max(self):
        self.first.current_health = 5
        self.first.assess_damage(-20)

        self.assertEquals(self.max_health, self.first.current_health )

    def test_ship_move_health_goes_up_one(self):
        self.first.current_health = 5
        self.first.move()

        self.assertEquals(6, self.first.current_health )

    def test_ship_move_health_doesnt_go_above_max(self):
        name = "Boaty McBoat Face"
        x = 1
        y = 2
        alignment = "something"
        max_health = 10
        range = 5
        attack_power = 20
        damage = -10
        
        first = Ship(name, x, y, alignment, max_health, range, attack_power)
        first.move()

        self.assertEquals(first.current_health, max_health)

if __name__ == '__main__':
    unittest.main()
