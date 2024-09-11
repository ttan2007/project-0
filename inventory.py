class Inventory:
    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            return True
        return False

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def has_item(self, item):
        return item in self.items

    def get_items(self):
        return self.items

    def is_full(self):
        return len(self.items) >= self.capacity

    def clear(self):
        self.items = []

    def __str__(self):
        return ", ".join(self.items) if self.items else "Empty"
