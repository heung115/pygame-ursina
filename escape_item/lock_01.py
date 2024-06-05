from ursina import *
from pathlib import Path
from escape_item.lock import Lock
from player import Player

model_path = Path("asset/escape_item/lock_1.obj")
player = Player()


class Lock1(Lock):
    def __init__(
        self,
        position=(0, 0, 0),
        rotation=(0, 0, 0),
        scale=1,
        lock_num=0,
        give_item=None,
    ):
        super().__init__(
            model=str(model_path),
            position=position,
            rotation=rotation,
            scale=scale,
            give_item=give_item,
        )
        self.lock_num = lock_num
        self.is_locked = True

    def unlock_action(self):
        print("Unlocking lock 1")
        if self.give_item != None:
            player.inventory.add_item(self.give_item)
        else:
            print("No item to give")
