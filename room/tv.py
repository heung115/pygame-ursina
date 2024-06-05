from ursina import *
from pathlib import Path
from escape_item.lock import Lock
from display_image.turn_image import TurnImage
from display_image.image_01 import Image_01

model_path = Path("asset/room/televisionModern.obj")


class TelevisionModern(Lock):
    def __init__(self, position, scale, rotation, lock_num, give_item=None):
        super().__init__(
            model=str(model_path),
            scale=(5),
            position=(6.5, 1.5, -9),
            rotation=(0, 180, 0),
            lock_num=lock_num,
            give_item=give_item,
        )
        self.image = Image(self)
        self.image.hide_image()
        self.image_show = False

    def unlock(self):
        if self.is_locked:
            self.is_locked = False
            self.unlock_action()

    def unlock_action(self):
        if self.image_show:
            self.image.hide_image()
            self.image_show = False

        else:
            self.image.show_image()
            self.image_show = True


class Image(TurnImage):
    def __init__(self, parent):
        super().__init__(
            "asset/image/image_01.jpeg",
            scale=(0.5, 0.3, 0.5),
            position=(0, 0.25, -0.025),
            parent=parent,
        )
        self.enabled = True
        self.parent
