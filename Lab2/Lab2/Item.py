class Item():
    def __init__(self, name, sku, cost):
        self.name = name
        self.sku = sku
        self._cost = cost

    def get_cost(self):
        return self._cost

    def set_cost(self, cost):
        self._cost = cost

    def __str__(self):
        return self.name + " - " + self.sku + " " + str(self.get_cost())

class BulkItem(Item):
    def __init__(self, name, sku, price_per_pound, number_of_pounds):
        super().__init__(name, sku, price_per_pound * number_of_pounds )
        self._price_per_pound = price_per_pound
        self._number_of_pounds = number_of_pounds

    def set_price_per_pound( price_per_pound ):
        self._cost = price_per_pound * self._number_of_pounds
        self._price_per_pound = price_per_pound

    def set_number_of_punds( number_of_pounds ):
        self._cost = number_of_pounds * self._price_per_pound
        self._number_of_pounds = number_of_pounds

class TaxableItem(Item):
    def __init__(self, name, sku, cost, tax_rate):
        super().__init__(name, sku, cost * tax_rate + cost )
        self._tax_rate = tax_rate

    def set_tax_rate(tax_rate):
         self._cost = self._cost / ( 1 + self._tax_rate ) * ( tax_rate + 1 )
         self._tax_rate = tax_rate

class PackageItem(Item):
    def __init__(self, name, sku, items):
        super().__init__(name, sku, sum( item.get_cost() for item in items ) )
        self._items = items
        #for item in items:
        #    self.cost += item.cost

    def add_item(self, item):
        self._items.append(item)

    def get_cost(self):
        return sum( item.get_cost() for item in self._items )

class ExceptionalItem(Item):
    def __init__(self, name, sku, cost):
        super().__init__(name, sku, cost)

    def get_cost(self):
        raise PermissionError("Invalid cost")

chocolate_chips = Item("Chocolate Chips", "123", 2.5)
oatmeal = BulkItem("Oatmeal", "234", 1.5, 3 )
water_bottle = TaxableItem("Water Bottle", "345", 3.75, .06 )
print(water_bottle)
water_bottle.tax_rate = .07
print(water_bottle)

gift_bag = PackageItem("Weird Gift", "456", [ chocolate_chips, oatmeal, water_bottle ] )

print(chocolate_chips)
print(oatmeal)
print(water_bottle)
print(gift_bag)

chocolate_chips.set_cost(3)

print(gift_bag)