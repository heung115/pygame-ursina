from ursina.prefabs.first_person_controller import FirstPersonController
from inventory import Inventory


class Player(FirstPersonController):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Player, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, **kwargs):
        if not hasattr(self, "initialized"):
            super().__init__(**kwargs)
            self.inventory = Inventory(capacity=5)
            self.initialized = True

    def on_collect(self, item):
        """아이템 수집 로직 처리"""
        print(f"Collecting {item.name}")
        if len(self.inventory.items) < self.inventory.capacity:
            self.inventory.add_item(item)
            item.disable()
        else:
            print("Inventory is full")
