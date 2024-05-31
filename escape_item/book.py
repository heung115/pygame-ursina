from ursina import *
from pathlib import Path
from display_image.image_01 import Image_01

model_path = Path("asset/escape_item/books.obj")

image = Image_01()
image.hide_image()


class Book(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=scale,
            position=position,
            collider="box",
            texture_scale=(10, 10),
            rotation=rotation,
        )
        self.image_show = False

    def input(self, key):
        if key == "right mouse down" and mouse.hovered_entity == self:
            if self.image_show:
                image.hide_image()
                self.image_show = False

            else:
                image.show_image()
                self.image_show = True
