from ursina import *
from inventory_item import InventoryItem
from player import Player
from escape_item.lock import Lock

player = Player()


class Key(InventoryItem):
    def __init__(
        self,
        model,
        position=(0, 0, 0),
        rotation=(0, 0, 0),
        scale=1,
        key_num=0,
        name="key",
        **kwargs,
    ):
        if not model:
            raise ValueError("Model must be provided")

        super().__init__(
            model=model,
            position=position,
            rotation=rotation,
            collider="box",
            scale=scale,
            **kwargs,
        )
        self.name = name
        self.key_num = key_num

    def use(self):
        target = player.get_view_target()
        print(f"target: {target}")
        if isinstance(target, Lock) and self.key_num == target.lock_num:
            print(f"useing {self.name} on {target.name} [lock_num: {target.lock_num}]")
            target.unlock()
            player.inventory.remove_item(self)
