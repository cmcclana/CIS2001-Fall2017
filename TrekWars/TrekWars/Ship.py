class Ship():
    def __init__(self, name, x, y, alignment, max_health, range, attack_power):
        self.name = name
        self.x_location = x
        self.y_location = y
        self.alsignment = alignment,
        self.max_health = max_health
        self.current_health = max_health
        self.range = range
        self.attack_power = attack_power

    def move(self):
        self.assess_damage(-1)

    def assess_damage(self, amount):
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0
        elif self.current_health > self.max_health:
            self.current_health = self.max_health


