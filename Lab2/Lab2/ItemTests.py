import unittest
from Item import *

class Test_ItemTests(unittest.TestCase):
    def test_item_init_and_get_cost(self):
        name = "Bread"
        sku = "123"
        cost = 1
        
        bread = Item(name, sku, cost)

        self.assertEqual(bread.name, name)
        self.assertEqual(bread.sku, sku)
        self.assertEqual(bread._cost, cost)
        self.assertEqual(bread.get_cost(), cost)

    def test_item_set_cost(self):
        name = "Bread"
        sku = "123"
        cost = 1
        new_cost = 2
        
        bread = Item(name, sku, cost)
        bread.set_cost(new_cost)

        self.assertEqual(bread.get_cost(), new_cost)

    def test_package_item(self):
        chocolate_chips = Item("Chocolate Chips", "123", 2.5)
        oatmeal = BulkItem("Oatmeal", "234", 1.5, 3 )
        water_bottle = TaxableItem("Water Bottle", "345", 3.75, .06 )

        gift_bag = PackageItem("Weird Gift", "456", [ chocolate_chips, oatmeal, water_bottle ] )

        self.assertEqual(gift_bag.get_cost(), 10.975)
        chocolate_chips.set_cost(3)
        self.assertEqual(gift_bag.get_cost(), 11.475)

    def test_package_item_add_item(self):
        name = "Gift Bag"
        sku = "987"
        pizza_cost = 5
        tax_rate = .06
        expected_cost = pizza_cost * ( tax_rate + 1 )
        pizza = TaxableItem("Pizza", "123", pizza_cost, tax_rate)
        gift_bag = PackageItem(name, sku, [])
        gift_bag.add_item(pizza)

        self.assertAlmostEqual(gift_bag.get_cost(), expected_cost)


    def test_exceptional_item(self):
        name = "Bread"
        sku = "123"
        cost = 1

        exceptional_item = ExceptionalItem(name, sku, cost)

        try:
            exceptional_item.get_cost()
            self.fail("no excpetion thrown")
        except PermissionError as e:
            self.assertEqual(e.args[0], "Invalid cost")

if __name__ == '__main__':
    unittest.main()
