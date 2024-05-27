# lock.py
from inventory_item import InventoryItem
from player import Player

player = Player()


class Lock(InventoryItem):
    def __init__(self, position=(0, 0, 0), scale=(1, 1, 1), rotation=(0, 0, 0)):
        super().__init__(
            model="Padlock.obj",
            position=position,
            scale=scale,
            rotation=rotation,
            collider="box",
            texture="white_cube",
            texture_scale=(10, 3),
            name="Padlock",
        )
        self.player = player

    def input(self, key):
        if key == "right mouse down" and self.hovered:
            print("Attempting to add lock to inventory...")
            if hasattr(self.player, "on_collect"):
                self.player.on_collect(self)
