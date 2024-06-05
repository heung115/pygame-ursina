from ursina import *
from pathlib import Path

model_path = Path("asset/room/deskCorner.obj")


class DeskCorner(Entity):
    def __init__(self, position, scale, rotation):
        super().__init__(
            model=str(model_path),
            scale=scale,
            position=position,
            collider="box",
            rotation=rotation,
        )
