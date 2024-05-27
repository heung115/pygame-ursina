from ursina.prefabs.first_person_controller import FirstPersonController
from inventory import Inventory


class Player(FirstPersonController):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Player, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, **kwargs):
        if self._initialized:
            return
        super().__init__(**kwargs)
        self.inventory = Inventory(capacity=5)
        self.inventory.create_ui()  # 인벤토리 UI 생성
        self._initialized = True

    def on_collect(self, item):
        print(f"Collecting {item.name}")
        if len(self.inventory.items) < self.inventory.capacity:
            self.inventory.add_item(item)
            item.disable()
        else:
            print("Inventory is full")
