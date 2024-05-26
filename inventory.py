from ursina import Entity


class Inventory:
    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Added {item} to inventory.")
        else:
            print("Inventory is full.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from inventory.")

    def list_items(self):
        return self.items
