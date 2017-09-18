class Item():
    def __init__(self, name, sku, cost):
        self.name = name
        self.sku = sku
        self.cost = cost

    def __str__(self):
        return self.name + " - " + self.sku + " " + str(self.cost)

class BulkItem(Item):
    def __init__(self, name, sku, price_per_pound, number_of_pounds):
        super().__init__(name, sku, price_per_pound * number_of_pounds )

class TaxableItem(Item):
    def __init__(self, name, sku, cost, tax_rate):
        super().__init__(name, sku, cost * tax_rate + cost )

class PackageItem(Item):
    def __init__(self, name, sku, items):
        super().__init__(name, sku, sum( item.cost for item in items ) )
        #for item in items:
        #    self.cost += item.cost

chocolate_chips = Item("Chocolate Chips", "123", 2.5)
oatmeal = BulkItem("Oatmeal", "234", 1.5, 3 )
water_bottle = TaxableItem("Water Bottle", "345", 3.75, .06 )

gift_bag = PackageItem("Weird Gift", "456", [ chocolate_chips, oatmeal, water_bottle ] )

print(chocolate_chips)
print(oatmeal)
print(water_bottle)
print(gift_bag)