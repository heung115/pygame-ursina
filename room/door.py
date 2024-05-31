from ursina import *
from pathlib import Path

model_path = Path("asset/room/doorway.obj")


class Door(Entity):
    def __init__(self, position=(0, 0, 0), scale=1):
        super().__init__(
            model=str(model_path),
            scale=scale,
            position=position,
            collider="box",
            texture_scale=(10, 10),
        )
