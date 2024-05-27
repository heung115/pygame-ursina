from ursina import *
from inventory_item import InventoryItem
from player import Player


player = Player()


class Key(InventoryItem):
    def __init__(
        self, model, position=(0, 0, 0), rotation=(0, 0, 0), scale=1, key_num=0
    ):
        if not model:
            raise ValueError("Model must be provided")

        super().__init__(
            model=model,
            position=position,
            rotation=rotation,
            collider="box",
            scale=scale,
        )
        self.key_num = key_num

    def input(self, key):
        if key == "right mouse down" and mouse.hovered_entity == self:
            player.inventory.add_item("key1", self.key_num)
            self.disable()
            print("Key collected!")
            self.display_message("Key collected!")
