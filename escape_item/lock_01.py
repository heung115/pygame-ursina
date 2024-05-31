from ursina import *
from pathlib import Path
from escape_item.lock import Lock

model_path = Path("asset/escape_item/lock_1.obj")


class Lock1(Lock):
    def __init__(self, position=(0, 0, 0), rotation=(0, 0, 0), scale=1, lock_num=0):
        super().__init__(
            model=str(model_path),
            position=position,
            rotation=rotation,
            scale=scale,
        )
        self.lock_num = lock_num
        self.is_locked = True
