from ursina import *
from pathlib import Path
from escape_item.lock import Lock
from player import Player

model_path = Path("asset/escape_item/lock_1.obj")
player = Player()


class DoorLock(Lock):
    def __init__(
        self,
        position=(0, 0, 0),
        rotation=(0, 0, 0),
        scale=1,
        lock_num=0,
        Door=None,
    ):
        super().__init__(
            model=str(model_path),
            position=position,
            rotation=rotation,
            scale=scale,
            give_item=None,
        )
        self.lock_num = lock_num
        self.is_locked = True
        self.door = Door

    def unlock_action(self):
        print("door open test")
        self.door.open()
