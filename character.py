class Character:
    def __init__(self, name, health, strength=10, defense=5):
        self.name = name
        self.health = health
        self.max_health = health
        self.strength = strength
        self.defense = defense
        self.inventory = []

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health = max(self.health - actual_damage, 0)
        return actual_damage

    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (HP: {self.health}/{self.max_health}, STR: {self.strength}, DEF: {self.defense})"