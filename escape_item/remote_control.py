from ursina import *
from pathlib import Path
from inventory_item import InventoryItem
from escape_item.key import Key

model_path = Path("asset/escape_item/Key_01.obj")


class RemoteControl(Key):
    def __init__(self, position, rotation, scale, key_num, name, **kwargs):
        super().__init__(
            model=str(model_path),
            position=position,
            rotation=rotation,
            scale=scale,
            key_num=key_num,
            name=name,
            **kwargs
        )
        self.icon_path = "asset/icon/remote_control_2.png"
