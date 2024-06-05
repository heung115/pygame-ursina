from ursina import *
from pathlib import Path

model_path = Path("asset/room/pottedPlant.obj")


class PottedPlant(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=(5),
            position=(-5, 0, -7),
            collider="box",
            texture_scale=(10, 10),
            rotation=(0, 0, 0),
        )