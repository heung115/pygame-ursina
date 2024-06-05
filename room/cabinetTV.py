from ursina import *
from pathlib import Path
from escape_item.lock import Lock
from display_image.display_image import DisplayImage

model_path = Path("asset/room/cabinetTelevision.obj")


class CabinetTelevision(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=(5),
            position=(8.5, 0, -8.5),
            collider="box",
            rotation=(0, 180, 0),
        )
        # image = DisplayImage(Path("asset/room/image_01.png"), scale=0.8)
