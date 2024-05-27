from ursina import *
from pathlib import Path
from inventory_item import InventoryItem
from player import Player
from escape_item.key import Key

model_path = Path("asset/escape_item/Key_01.obj")

player = Player()


class Key1(Key):
    def __init__(self, position=(0, 0, 0), rotation=(0, 0, 0), scale=1, key_num=0):
        super().__init__(
            model=str(model_path),
            position=position,
            rotation=rotation,
            scale=scale,
            key_num=key_num,
        )
